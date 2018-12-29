import utilities
import os
from settings import *

def test_get_unique_color_list():

    # list may look inflated, but the output map is scaled.

    expected_list = [(0, 0, 0), (255, 255, 255), (0, 0, 255), (255, 0, 0), (0, 255, 0)]

    actual_list = utilities.get_unique_color_list(os.path.join(TEST_FOLDER, "testmap.png"))

    assert repr(actual_list) == repr(expected_list)

def test_get_color_map_list():
    pass
