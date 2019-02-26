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


# some global directories for these tests
EXAMPLE_PROJECT = os.path.join(OUTPUT_FOLDER, "w4Wd3k6SiogHe1")
EXAMPLE_PROJECT_SPRITES = os.path.join(EXAMPLE_PROJECT, "sprites")
EXAMPLE_PROJECT_LEVELS = os.path.join(EXAMPLE_PROJECT, "levels")

# some global files for these tests
EXAMPLE_PROJECT_CLASSES = os.path.join(EXAMPLE_PROJECT, "classes.py")
EXAMPLE_PROJECT_GAME = os.path.join(EXAMPLE_PROJECT, "w4Wd3k6SiogHe1.py")
EXAMPLE_PROJECT_SETTINGS = os.path.join(EXAMPLE_PROJECT, "settings.py")
EXAMPLE_PROJECT_TESTMAP1 = os.path.join(EXAMPLE_PROJECT_LEVELS, "testmap.p")
EXAMPLE_PROJECT_TESTMAP2 = os.path.join(EXAMPLE_PROJECT_LEVELS, "testmap2.p")


def test_create_new_game():
    """
    Test to ensure the game files are created properly
    This code also covers the additional methods:
     - copy_necessary_files
     - create_map
     - create_pygame_classes
     - create_main_game_code
     - set_unique_colors_list
    """

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

    files = [EXAMPLE_PROJECT, EXAMPLE_PROJECT_LEVELS, EXAMPLE_PROJECT_SPRITES, EXAMPLE_PROJECT_CLASSES, EXAMPLE_PROJECT_GAME, EXAMPLE_PROJECT_SETTINGS]

    # check if file path exists
    for file in files:
        assert os.path.exists(file)

def test_get_existing_color_list_before_add_map():
    """Ensure the color list is created properly before adding a map"""

    actual_list = game_gen.get_existing_color_list(EXAMPLE_PROJECT_LEVELS)
    test_list = [(0,0,0), (255,255,255), (0,0,255), (255,0,0), (0,255,0)]

    assert actual_list == test_list

def test_add_map_to_project_with_new_colors():
    """
    Test to ensure the game files are created properly
    This code also covers the additional methods:
     - copy_necessary_files
     - create_map
     - create_pygame_classes
     - create_main_game_code
     - set_unique_colors_list
    """

    inputs = io.StringIO(
    # name of the project
    'w4Wd3k6SiogHe1\n'+
    # name for the new map
    'testmap2\n'+
    # image for the new map
    'yellow.png\n'+
    # input for get_color_dict
    'sand\nsand.png\n')

    # run add_map_to_project with inputs
    with replace_stdin(inputs):
        game_gen.add_map_to_project()

    assert os.path.exists(EXAMPLE_PROJECT_TESTMAP2)

def test_get_existing_color_list_after_add_map():
    """Ensure the color list is appended to properly after adding a map"""

    actual_list = game_gen.get_existing_color_list(EXAMPLE_PROJECT_LEVELS)
    test_list = [(0,0,0), (255,255,255), (0,0,255), (255,0,0), (0,255,0), (230,230,19)]

    assert actual_list == test_list

def test_create_pygame_classes():
    """test the contents of the generated classes"""

    # open file and read contents, compare to expected values
    try:
        with open(EXAMPLE_PROJECT_CLASSES) as reader:
            file = reader.readlines()

            # test random line numbers against what is expected
            for count, line in enumerate(file):
                if count == 0:
                    assert "import pygame as pg\n" == line
                elif count == 1:
                    assert "from settings import *\n" == line
                # assert that the first class was created correctly
                elif count == 3:
                    assert "class sand(pg.sprite.Sprite):\n" == line
                elif count == 4:
                    assert "    def __init__(self, game, x, y):\n" == line
                elif count == 5:
                    assert "        self.groups = game.background_sprites\n"
                elif count == 6:
                    assert "        pg.sprite.Sprite.__init__(self, self.groups)\n" == line
                elif count == 7:
                    assert "        self.game = game\n"
                elif count == 8:
                    assert "        self.image = game.sand_img\n" == line
                elif count == 9:
                    assert "        self.rect = self.image.get_rect()\n" == line
                elif count == 10:
                    assert "        self.x = x\n" == line
                elif count == 11:
                    assert "        self.y = y\n" == line



    except Exception as e:
        print(e)
        assert True == False

def test_create_main_game_code():
    """test the contents of the created game code"""
    pass

    rmtree(EXAMPLE_PROJECT)

@contextmanager
def replace_stdin(target):
    """use a context manager to change the value of sys.stdin and then revert it back"""
    orig = sys.stdin
    sys.stdin = target
    yield
    sys.stdin = orig
