import numpy as np
import circlehough.hough_transformation as ht
import math

def test_apply_triangular_evaluation():
    ring_radius = 5
    r_point = 4.5
    amplitude = 1
    hough_epsilon = 1
    result_value = ht.py_apply_triangular_evaluation(
        r_point, hough_epsilon, ring_radius, amplitude)
    assert result_value == 0.5


def test_calculate_point_distance():
    ring_cx = 0
    ring_cy = 0
    point_x = 0
    point_y = 1
    r_point = ht.py_calculate_point_distance(
        ring_cx, ring_cy, point_x, point_y)
    assert r_point == 1


def test_sum_point_contributions():
    point_positions = np.array([
        [1, 0], [0, 1], [0.5, 0], [0, 0.5],
        [1.5, 0], [0, 1.5], [2, 0], [0, 2],
        [2.5, 0], [0, 2.5], [3, 0], [0, 3]
    ], dtype=np.float32)
    cx = np.float32(0)
    cy = np.float32(0)
    r = np.float32(2)
    hough_epsilon = 1.
    total_amplitude = ht.py_sum_point_contributions(
        point_positions, cx, cy, r, hough_epsilon)
    assert total_amplitude == 4


def test_hough_transform_ring():
    point_positions = np.array([
        [2, 0], [0, 2], [-2, 0], [0, -2],
        [math.sqrt(2), math.sqrt(2)], [math.sqrt(2), -math.sqrt(2)],
        [-math.sqrt(2), math.sqrt(2)], [-math.sqrt(2), -math.sqrt(2)]
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