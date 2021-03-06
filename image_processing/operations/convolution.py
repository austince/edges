""" Various functions to convolve 
"""
import numpy as np


def convolve_replicate_bounds_point(x, y, image, kernel, constant=1):
    """

    :param x:
    :param y:
    :param image:
    :param kernel:
    :param constant:
    :return:
    """
    max_x, max_y = image.shape
    k_max_x, k_max_y = kernel.shape
    k_max_x = int(k_max_x / 2)
    k_max_y = int(k_max_y / 2)

    convolve_sum = np.int64(0)

    for k_x in range(-k_max_x, k_max_x + 1):
        for k_y in range(-k_max_y, k_max_y + 1):
            adj_x = k_x + x
            adj_y = k_y + y

            if adj_x < 0:
                adj_x = 0
            elif adj_x >= max_x:
                adj_x = max_x - 1

            if adj_y < 0:
                adj_y = 0
            elif adj_y >= max_y:
                adj_y = max_y - 1

            iter_sum = kernel[k_x + k_max_x][k_y + k_max_y] * image[adj_x][adj_y]
            convolve_sum += iter_sum

    return convolve_sum * constant


def convolve_replicate_bounds(image, kernel, constant=1):
    """
    convolved[x][y]

    :param image:
    :param kernel:
    :param constant:
    :return:
    """
    max_x = image.shape[0]
    max_y = image.shape[1]
    convolved = image.copy()

    for x in range(0, max_x):
        for y in range(0, max_y):
            convolved[x][y] = convolve_replicate_bounds_point(x, y, image, kernel, constant)

    return convolved
