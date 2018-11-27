from circlehough import hough
import math
import numpy as np


def test_get_bin_centers():
    c_x = 5
    c_y = 5
    r = 5
    uncertainty = 10
    cx_bin_centers, cy_bin_centers, r_bin_centers = hough.get_bin_centers( 
        c_x, c_y, r, uncertainty)
    assert cx_bin_centers.all() == np.array(list(range(11))).all()
    assert cy_bin_centers.all() == np.array(list(range(11))).all()
    assert r_bin_centers.all() == np.array(list(range(11))).all()


def test_interpretHoughSpace():
    houghSpace = np.array([
        [np.array([0,1,2]), np.array([3,8,5]), np.array([6,7,4])],
        [np.array([0,1,2]), np.array([3,9,5]), np.array([6,7,4])],
        [np.array([0,1,2]), np.array([3,10,5]), np.array([6,7,4])]])
    assert hough.interpretHoughSpace(houghSpace) == (2,1,1)


def test_advanced_guess_with_hough():
    guessed_cx = 1
    guessed_cy = 1
    guessed_r = 2
    point_cloud  = np.array([
        [2, 0], [0, 2], [-2, 0], [0, -2],
        [math.sqrt(2), math.sqrt(2)], [math.sqrt(2), -math.sqrt(2)],
        [-math.sqrt(2), math.sqrt(2)], [-math.sqrt(2), -math.sqrt(2)],
    ])
    uncertainty = 2
    epsilon = 0.2
    hough_cx, hough_cy, hough_r = hough.advanced_guess_with_hough(
        guessed_cx, guessed_cy, guessed_r, point_cloud,
        uncertainty, epsilon
        )
    assert hough_cx == 0
    assert hough_cy == 0
    assert hough_r == 2