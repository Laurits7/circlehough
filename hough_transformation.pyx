from distutils.core import setup
from Cython.Build import cythonize
import numpy as np
cimport numpy as np
from libc.math cimport sqrt
cimport cython


@cython.boundscheck(False)
@cython.wraparound(False)
def hough_transform_ring(
    np.ndarray[np.float64_t, ndim=2] point_positions,
    np.ndarray[np.float64_t, ndim=1] cx_bin_centers,
    np.ndarray[np.float64_t, ndim=1] cy_bin_centers,
    np.ndarray[np.float64_t, ndim=1] r_bin_centers,
    np.float64_t hough_epsilon
):
    cdef int i_cx = 0
    cdef int i_cy = 0
    cdef int i_r = 0
    cdef int cx_max = cx_bin_centers.shape[0]
    cdef int cy_max = cy_bin_centers.shape[0]
    cdef int r_max = r_bin_centers.shape[0]
    cdef np.float64_t cx, cy, r 
    cdef np.float64_t contribution
    cdef np.ndarray[np.float64_t, ndim=3] houghSpace = np.zeros(
        [cx_max, cy_max, r_max],
        dtype=np.float64
    )
    for i_cx in range(cx_max):
        for i_cy in range(cy_max):
            for i_r in range(r_max):
                i_r +=1
                contribution = sum_photon_contributions(
                    point_positions, 
                    cx_bin_centers[i_cx],
                    cy_bin_centers[i_cy], 
                    r_bin_centers[i_r], 
                    hough_epsilon
                )
                houghSpace[i_cx, i_cy, i_r] = contribution
    return houghSpace


@cython.boundscheck(False)
@cython.wraparound(False)
cdef np.float64_t sum_photon_contributions(
    np.ndarray[np.float64_t, ndim=2] photon_positions,
    np.float64_t cx, 
    np.float64_t cy, 
    np.float64_t r, 
    np.float64_t hough_epsilon
):
    cdef np.float64_t total_amplitude = 0
    cdef np.float64_t photon_x
    cdef np.float64_t photon_y
    cdef np.float64_t r_photon
    cdef np.float64_t photon_contribution
    photon_positions_max = photon_positions.shape[0]
    for i_photon in range(photon_positions_max):
        photon_x = photon_positions[i_photon, 0]
        photon_y = photon_positions[i_photon, 1]
        r_photon = calculate_photon_distance(
            ring_cx=cx, ring_cy=cy,
            photon_x=photon_x, photon_y=photon_y)
        photon_contribution = apply_triangular_evaluation(
            ring_radius=r, amplitude=1,
            r_photon=r_photon, hough_epsilon=hough_epsilon)
        total_amplitude += photon_contribution
    return total_amplitude


@cython.boundscheck(False)
@cython.wraparound(False)
cdef np.float64_t apply_triangular_evaluation(
    np.float64_t r_photon,
    np.float64_t hough_epsilon,
    np.float64_t ring_radius,
    np.float64_t amplitude
):
    cdef np.float64_t abs_loc
    cdef np.float64_t photon_contribution
    if (
        r_photon > ring_radius-hough_epsilon and
        r_photon < ring_radius+hough_epsilon
    ):
        abs_loc = abs(r_photon-ring_radius)
        photon_contribution = amplitude*(
            hough_epsilon-abs_loc)/(hough_epsilon)
    else:
        photon_contribution = 0
    return photon_contribution


@cython.boundscheck(False)
@cython.wraparound(False)
cdef np.float64_t calculate_photon_distance(
    np.float64_t ring_cx,
    np.float64_t ring_cy,
    np.float64_t photon_x,
    np.float64_t photon_y
):
    cdef np.float64_t x_pos = photon_x-ring_cx
    cdef np.float64_t y_pos = photon_y-ring_cy
    cdef np.float64_t r_photon = sqrt(x_pos**2 + y_pos**2)
    return r_photon
