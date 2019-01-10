from PIL import Image
import os
from settings import *
import pickle

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

def return_updated_list(old_color_list, new_color_list):
    """This method compares two lists and finds values that are not apart of the first list, but are in the second"""

    new_tile_flag = False
    new_colors = []

    for color in new_color_list:
        if color not in old_color_list:
            old_color_list.append(color)
            new_colors.append(color)
            new_tile_flag = True

    return old_color_list, new_tile_flag, new_colors


def write_file(new_lines, file_name):
    """This method writes information in the form of a list of lines to the file specified by file_name"""
    try:
        print("\n[utilities] Writing the file: ", file_name, "...")
        file = open(file_name, "w")

        for line in new_lines:
            file.write(line)

        file.close()

        print("[utilities] Done!")

    except BaseException:
        print("\n[utilities] Writing the file encountered an error.\n")
