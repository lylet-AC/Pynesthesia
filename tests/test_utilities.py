import utilities
from PIL import Image
import pickle
import os
# local imports
from settings import *
from utilities import *

def test_get_path_if_valid():
    pass

def test_get_image_if_valid():
    pass

def test_get_color_dict():
    pass

def test_get_unique_color_list():
    """Gather a list of expected values and compare them against the output of the function"""

    # get the image first
    image = Image.open(os.path.join(TEST_FOLDER, "testmap.png"))

    # set up the expected and actual lists
    expected_list = [(0, 0, 0), (0, 255, 0), (255, 0, 0), (255, 255, 255)]
    actual_list = utilities.get_unique_color_list(image)

    # compare lists
    assert repr(actual_list) == repr(expected_list)

def test_get_color_map_list():
    """Use the testmap.png to ensure the color map list is correct"""

    image = Image.open(os.path.join(TEST_FOLDER, "testmap.png"))
    actual_list = utilities.get_color_map_list(image)

    # a representation of the images' colors with RGB tuples
    expected_list = [
    [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)], # row of black
    [(0, 255, 0), (0, 255, 0), (0, 255, 0), (0, 255, 0)], # row of green
    [(255, 0, 0), (255, 0, 0), (255, 0, 0), (255, 0, 0)], # row of red
    [(255, 255, 255), (255, 255, 255), (255, 255, 255), (255, 255, 255)] # row of white
    ]

    assert repr(actual_list) == repr(expected_list)

def test_return_updated_list():
    """Use two lists to test expected output of return_updated_list"""
    # Expected output is:
    # 1.) list of unique colors with new colors added
    # 2.) flag that is true if a new color is in the new list
    # 3.) list containing only the added colors

    old_list = [(255, 255, 255), (0, 0, 0), (0, 0, 255)]
    new_list = [(255, 255, 255), (0, 0, 0), (255, 0, 0)]

    updated_list, new_color_flag, new_colors = utilities.return_updated_list(old_list, new_list)

    # should be the same as the old_list with any data appended to it
    assert repr(updated_list) == [(255, 255, 255), (0, 0, 0), (0, 0, 255), (255, 0, 0)]
    # new color exists in new_list so this should be true
    assert repr(new_color_flag) == True
    # this only contains the elements of new_list that are not in old_list
    assert repr(new_colors) == [(255, 0, 0)]

def test_write_file():
    pass
