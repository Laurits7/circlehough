from muons import make_triangular_distribution as mtd
import math
import numpy as np


def test_apply_triangular_evaluation():
    ring_radius = 5
    r_photon = 4.5
    amplitude = 1
    hough_epsilon = 1
    result_value = mtd.apply_triangular_evaluation(
        r_photon, hough_epsilon, ring_radius, amplitude)
    assert result_value == 0.5


def test_calculate_photon_distance():
    ring_cx = 0
    ring_cy = 0
    photon_x = 0
    photon_y = 1
    r_photon = mtd.calculate_photon_distance(
        ring_cx, ring_cy, photon_x, photon_y)
    assert r_photon == 1


def test_sum_photon_contributions():
    photon_positions = [
        [1, 0, 10], [0, 1, 7], [0.5, 0, 8], [0, 0.5, 7], [1.5, 0, 6], [0, 1.5, 5],
        [2, 0, 4], [0, 2, 3], [2.5, 0, 2], [0, 2.5, 1], [3, 0, 0], [0, 3, 11]
    ]
    cx = 0
    cy = 0
    r = 2
    hough_epsilon = 1
    total_amplitude = mtd.sum_photon_contributions(photon_positions, cx, cy, r, hough_epsilon)
    assert total_amplitude == 4


def test_hough_transform_ring():
    point_positions = [
        [2, 0, 10], [0, 2, 7], [-2, 0, 8], [0, -2, 7], [math.sqrt(2), math.sqrt(2), 6],
        [math.sqrt(2), -math.sqrt(2), 5], [-math.sqrt(2), math.sqrt(2), 4],
        [-math.sqrt(2), -math.sqrt(2), 3],
    ]
    cx_bin_centers = np.array(list(range(-3, 4)))
    cy_bin_centers = np.array(list(range(-3, 4)))
    r_bin_centers = np.array(list(range(5)))
    hough_epsilon = 1
    houghSpace = mtd.hough_transform_ring(
        point_positions,
        cx_bin_centers,
        cy_bin_centers,
        r_bin_centers,
        hough_epsilon
    )
    indices_of_maximum_value = np.unravel_index(
        np.argmax(houghSpace), dims=houghSpace.shape)
    assert indices_of_maximum_value == (3, 3, 2)


def test_get_bin_centers():
    c_x = 5
    c_y = 5
    r = 5
    uncertainty = 10
    cx_bin_centers, cy_bin_centers, r_bin_centers = mtd.get_bin_centers( 
        c_x, c_y, r, uncertainty)
    assert cx_bin_centers.all() == np.array(list(range(11))).all()
    assert cy_bin_centers.all() == np.array(list(range(11))).all()
    assert r_bin_centers.all() == np.array(list(range(11))).all()


def test_interpretHoughSpace():
    houghSpace = np.array([
        [np.array([0,1,2]), np.array([3,8,5]), np.array([6,7,4])],
        [np.array([0,1,2]), np.array([3,9,5]), np.array([6,7,4])],
        [np.array([0,1,2]), np.array([3,10,5]), np.array([6,7,4])]])
    assert mtd.interpretHoughSpace(houghSpace) == (2,1,1)


def test_advanced_guess_with_hough():
    guessed_cx = 1
    guessed_cy = 1
    guessed_r = 2
    point_cloud  = np.array([
        [2, 0, 10], [0, 2, 7], [-2, 0, 8], [0, -2, 7], [math.sqrt(2), math.sqrt(2), 6],
        [math.sqrt(2), -math.sqrt(2), 5], [-math.sqrt(2), math.sqrt(2), 4],
        [-math.sqrt(2), -math.sqrt(2), 3],
    ])
    uncertainty = 2
    epsilon = 0.2
    hough_cx, hough_cy, hough_r = mtd.advanced_guess_with_hough(
        guessed_cx, guessed_cy, guessed_r, point_cloud,
        uncertainty, epsilon
        )
    assert hough_cx == 0
    assert hough_cy == 0
    assert hough_r == 2