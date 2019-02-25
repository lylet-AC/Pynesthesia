from PIL import Image
import pickle
import os
import io
import sys
from shutil import rmtree
from contextlib import contextmanager
# local imports
from settings import *
import game_gen


def test_create_new_game():

    inputs = io.StringIO(
        # name of the game
        'w4Wd3k6SiogHe1\n'+
        # image for the map
        'testmap.png\n'+
        # name for the map
        'testmap\n'+
        # input for get_color_dict
        'wall\nwall.png\nbarrel\nbarrel.png\ntree\ntree.png\ntile\ntile.png\nwater\nwater.png\n')

    # run create_new_game with the inputs
    with replace_stdin(inputs):
        game_gen.create_new_game()

    # paths that should exist
    EXAMPLE_PROJECT = os.path.join(OUTPUT_FOLDER, "w4Wd3k6SiogHe1")
    EXAMPLE_PROJECT_SPRITES = os.path.join(EXAMPLE_PROJECT, "sprites")
    EXAMPLE_PROJECT_LEVELS = os.path.join(EXAMPLE_PROJECT, "levels")
    EXAMPLE_PROJECT_CLASSES = os.path.join(EXAMPLE_PROJECT, "classes.py")
    EXAMPLE_PROJECT_GAME = os.path.join(EXAMPLE_PROJECT, "w4Wd3k6SiogHe1.py")
    EXAMPLE_PROJECT_SETTINGS = os.path.join(EXAMPLE_PROJECT, "settings.py")

    files = [EXAMPLE_PROJECT, EXAMPLE_PROJECT_LEVELS, EXAMPLE_PROJECT_SPRITES, EXAMPLE_PROJECT_CLASSES, EXAMPLE_PROJECT_GAME, EXAMPLE_PROJECT_SETTINGS]

    # check if file path exists
    for file in files:
        assert os.path.exists(file)

    rmtree(EXAMPLE_PROJECT)

def test_copy_necessary_files():
    pass


def test_set_unique_colors_list():
    pass


def test_get_existing_color_list():
    pass


def test_create_map():
    pass


def test_add_map_to_project():
    pass


def test_create_pygame_classes():
    pass


def test_create_main_game_code():
    pass

@contextmanager
def replace_stdin(target):
    """use a context manager to change the value of sys.stdin and then revert it back"""
    orig = sys.stdin
    sys.stdin = target
    yield
    sys.stdin = orig
