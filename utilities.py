from PIL import Image
import os
from settings import *

def get_unique_color_list(input_image):
    """This method obtains a list of unique colors in the input list"""
    pix = input_image.load()

    unique_list = []

    width, height = input_image.size

    for w in range(width):
        for h in range(height):
            if pix[w, h] not in unique_list:
                unique_list.append(pix[w, h])

    return unique_list


def get_color_map_list(input_image):
    """This method gathers a representation of the input image as list of lists containing the color data for each line of the input image"""
    pix = input_image.load()

    map_list = []

    width, height = input_image.size

    for w in range(width):
        map_list.append([])
        for h in range(height):
            map_list[w].append(pix[w, h])

    return map_list
