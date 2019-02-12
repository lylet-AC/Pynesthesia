from PIL import Image
import pickle
import os
import io
import sys
from contextlib import contextmanager
# local imports
from settings import *
import utilities

def test_get_path_if_valid_files():
    """test that the get_path_if_valid function does indeed return the correct path"""

    # try to open the README.md at the root of Pynesthesia
    with replace_stdin(io.StringIO("README.md")):
        file = utilities.get_path_if_valid("test prompt", type="file", path=ROOT_FOLDER)

    # try to open Pynesthesia.py at the root of Pynesthesia
    with replace_stdin(io.StringIO("Pynesthesia.py")):
        file2 = utilities.get_path_if_valid("test prompt", type="file", path=ROOT_FOLDER)

    # assert that the file paths were returned and match
    assert file == os.path.join(ROOT_FOLDER, "README.md")
    assert file2 == os.path.join(ROOT_FOLDER, "Pynesthesia.py")

def test_get_image_if_valid():
    """test that the function returns the correct image file"""

    # our image opened directly
    actual_img = Image.open(os.path.join(TEST_FOLDER, "testmap.png"))

    # image opened with the method in utilities
    with replace_stdin(io.StringIO(TEST_IMAGE)):
        test_img = utilities.get_image_if_valid("test prompt", "testmap.png")

    # ensure they are the same size
    assert test_img.size == test_img.size
    # ensure the unique color lists are the same
    assert utilities.get_unique_color_list(test_img) == utilities.get_unique_color_list(actual_img)
    # ensure the whole map lists are the same
    assert utilities.get_color_map_list(test_img) == utilities.get_color_map_list(actual_img)

def test_get_color_dict():
    """create simulated inputs and test that the color dict is being generated properly"""

    # list of simulated inputs
    input_list = ["wall.png", "wall", "barrel.png", "barrel", "tree.png", "tree", "tile.png", "tile"]

    for input in input_list:
        with replace_stdin(io.StringIO(input)):
            pass

    #TODO: Find a way to load all of these values into the input buffer
    #NOTE: The input buffer works like a filereader, therefore if we can use StringIO to
    #store these values in a series, they will simultaniously be run when needed.

    pass

def test_get_unique_color_list():
    """Gather a list of expected values and compare them against the output of the function"""

    # get the image first
    image = Image.open(os.path.join(TEST_FOLDER, "testmap.png"))

    # set up the expected and actual lists
    expected_list = [(0, 0, 0), (0, 255, 0), (255, 0, 0), (255, 255, 255)]
    actual_list = utilities.get_unique_color_list(image)

    # compare lists
    assert actual_list == expected_list

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

    assert actual_list == expected_list

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
    assert updated_list == [(255, 255, 255), (0, 0, 0), (0, 0, 255), (255, 0, 0)]
    # new color exists in new_list so this should be true
    assert new_color_flag == True
    # this only contains the elements of new_list that are not in old_list
    assert new_colors == [(255, 0, 0)]

def test_write_file():
    pass

@contextmanager
def replace_stdin(target):
    """use a context manager to change the value of sys.stdin and then revert it back"""
    orig = sys.stdin
    sys.stdin = target
    yield
    sys.stdin = orig
