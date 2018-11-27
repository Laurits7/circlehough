import numpy as np
import circlehough.hough_transformation as ht
import math

def test_apply_triangular_evaluation():
    ring_radius = 5
    r_photon = 4.5
    amplitude = 1
    hough_epsilon = 1
    result_value = ht.py_apply_triangular_evaluation(
        r_photon, hough_epsilon, ring_radius, amplitude)
    assert result_value == 0.5


def test_calculate_photon_distance():
    ring_cx = 0
    ring_cy = 0
    photon_x = 0
    photon_y = 1
    r_photon = ht.py_calculate_photon_distance(
        ring_cx, ring_cy, photon_x, photon_y)
    assert r_photon == 1


def test_sum_photon_contributions():
    photon_positions = np.array([
        [1, 0, 10], [0, 1, 7], [0.5, 0, 8], [0, 0.5, 7],
        [1.5, 0, 6], [0, 1.5, 5], [2, 0, 4], [0, 2, 3],
        [2.5, 0, 2], [0, 2.5, 1], [3, 0, 0], [0, 3, 11]
    ], dtype=np.float32)
    cx = np.float32(0)
    cy = np.float32(0)
    r = np.float32(2)
    hough_epsilon = 1.
    total_amplitude = ht.py_sum_photon_contributions(
        photon_positions, cx, cy, r, hough_epsilon)
    assert total_amplitude == 4


def test_hough_transform_ring():
    point_positions = np.array([
        [2, 0, 10], [0, 2, 7], [-2, 0, 8], [0, -2, 7],
        [math.sqrt(2), math.sqrt(2), 6], [math.sqrt(2), -math.sqrt(2), 5],
        [-math.sqrt(2), math.sqrt(2), 4], [-math.sqrt(2), -math.sqrt(2), 3]
    ], dtype=np.float32)
    cx_bin_centers = np.array(list(range(-3, 4)), dtype=np.float32)
    cy_bin_centers = np.array(list(range(-3, 4)), dtype=np.float32)
    r_bin_centers = np.array(list(range(5)), dtype=np.float32)
    hough_epsilon = 1
    houghSpace = ht.hough_transform_ring(
        point_positions,
        cx_bin_centers,
        cy_bin_centers,
        r_bin_centers,
        hough_epsilon
    )
    indices_of_maximum_value = np.unravel_index(
        np.argmax(houghSpace), dims=houghSpace.shape)
    assert indices_of_maximum_value == (3, 3, 2)