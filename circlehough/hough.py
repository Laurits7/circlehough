import numpy as np
from .hough_transformation import hough_transform_ring


def get_bin_centers(
    c_x, c_y, r, uncertainty
):
    cx_bin_centers = np.linspace(
        start=c_x - 0.5*uncertainty,
        stop=c_x + 0.5*uncertainty,
        num=11)
    cy_bin_centers = np.linspace(
        start=c_y - 0.5*uncertainty,
        stop=c_y + 0.5*uncertainty,
        num=11)
    r_bin_centers = np.linspace(
        start=r - 0.5*uncertainty,
        stop=r + 0.5*uncertainty,
        num=11)
    return cx_bin_centers, cy_bin_centers, r_bin_centers


def interpretHoughSpace(
    houghSpace
):
    indices_of_maximum_value = np.unravel_index(
        np.argmax(houghSpace), dims=houghSpace.shape)
    return indices_of_maximum_value


def advanced_guess_with_hough(
    guessed_cx, guessed_cy, guessed_r, point_cloud,
    uncertainty, epsilon
):
    cx_bin_centers, cy_bin_centers, r_bin_centers = (
        get_bin_centers(guessed_cx, guessed_cy, guessed_r, uncertainty)
    )
    epsilon = np.float32(epsilon)
    cx_bin_centers = cx_bin_centers.astype(np.float32)
    cy_bin_centers = cy_bin_centers.astype(np.float32)
    r_bin_centers = r_bin_centers.astype(np.float32)
    point_positions = point_cloud.astype(np.float32)
    houghSpace = hough_transform_ring(
        point_positions, cx_bin_centers,
        cy_bin_centers, r_bin_centers, epsilon
    )
    location_for_maxima = interpretHoughSpace(houghSpace)
    hough_cx_idx = int(location_for_maxima[0])
    hough_cy_idx = int(location_for_maxima[1])
    hough_r_idx = int(location_for_maxima[2])
    hough_cx = cx_bin_centers[hough_cx_idx]
    hough_cy = cy_bin_centers[hough_cy_idx]
    hough_r = r_bin_centers[hough_r_idx]
    return hough_cx, hough_cy, hough_r
