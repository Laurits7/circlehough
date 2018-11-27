from distutils.core import setup
from Cython.Build import cythonize
import numpy as np
cimport numpy as np
from libc.math cimport sqrt
cimport cython


@cython.boundscheck(False)
@cython.wraparound(False)
def hough_transform_ring(
    np.ndarray[np.float32_t, ndim=2] point_positions,
    np.ndarray[np.float32_t, ndim=1] cx_bin_centers,
    np.ndarray[np.float32_t, ndim=1] cy_bin_centers,
    np.ndarray[np.float32_t, ndim=1] r_bin_centers,
    np.float32_t hough_epsilon
):
    cdef int i_cx = 0
    cdef int i_cy = 0
    cdef int i_r = 0
    cdef int cx_max = cx_bin_centers.shape[0]
    cdef int cy_max = cy_bin_centers.shape[0]
    cdef int r_max = r_bin_centers.shape[0]
    cdef np.float32_t cx, cy, r 
    cdef np.float32_t contribution
    cdef np.ndarray[np.float32_t, ndim=3] houghSpace = np.zeros(
        [cx_max, cy_max, r_max],
        dtype=np.float32
    )
    for i_cx in range(cx_max):
        for i_cy in range(cy_max):
            for i_r in range(r_max):
                i_r +=1
                contribution = sum_point_contributions(
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
cdef np.float32_t sum_point_contributions(
    np.ndarray[np.float32_t, ndim=2] point_positions,
    np.float32_t cx, 
    np.float32_t cy, 
    np.float32_t r, 
    np.float32_t hough_epsilon
):
    cdef np.float32_t total_amplitude = 0
    cdef np.float32_t point_x
    cdef np.float32_t point_y
    cdef np.float32_t r_point
    cdef np.float32_t point_contribution
    point_positions_max = point_positions.shape[0]
    for i_point in range(point_positions_max):
        point_x = point_positions[i_point, 0]
        point_y = point_positions[i_point, 1]
        r_point = calculate_point_distance(
            ring_cx=cx, ring_cy=cy,
            point_x=point_x, point_y=point_y)
        point_contribution = apply_triangular_evaluation(
            ring_radius=r, amplitude=1,
            r_point=r_point, hough_epsilon=hough_epsilon)
        total_amplitude += point_contribution
    return total_amplitude


def py_sum_point_contributions(
    point_positions,
    cx,
    cy,
    r,
    hough_epsilon
):
    total_amplitude = sum_point_contributions(
        point_positions,
        cx,
        cy,
        r,
        hough_epsilon
    )
    return total_amplitude



@cython.boundscheck(False)
@cython.wraparound(False)
cdef np.float32_t apply_triangular_evaluation(
    np.float32_t r_point,
    np.float32_t hough_epsilon,
    np.float32_t ring_radius,
    np.float32_t amplitude
):
    cdef np.float32_t abs_loc
    cdef np.float32_t point_contribution
    if (
        r_point > ring_radius-hough_epsilon and
        r_point < ring_radius+hough_epsilon
    ):
        abs_loc = abs(r_point-ring_radius)
        point_contribution = amplitude*(
            hough_epsilon-abs_loc)/(hough_epsilon)
    else:
        point_contribution = 0
    return point_contribution


def py_apply_triangular_evaluation(
    r_point,
    hough_epsilon,
    ring_radius,
    amplitude
):
    point_contribution = apply_triangular_evaluation(
        r_point,
        hough_epsilon,
        ring_radius,
        amplitude
    )
    return point_contribution


@cython.boundscheck(False)
@cython.wraparound(False)
cdef np.float32_t calculate_point_distance(
    np.float32_t ring_cx,
    np.float32_t ring_cy,
    np.float32_t point_x,
    np.float32_t point_y
):
    cdef np.float32_t x_pos = point_x-ring_cx
    cdef np.float32_t y_pos = point_y-ring_cy
    cdef np.float32_t r_point = sqrt(x_pos**2 + y_pos**2)
    return r_point


def py_calculate_point_distance(
    ring_cx,
    ring_cy,
    point_x,
    point_y
):
    r_point = calculate_point_distance(
        ring_cx,
        ring_cy,
        point_x,
        point_y
    )
    return r_point