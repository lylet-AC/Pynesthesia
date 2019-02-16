import utilities
import PIL
import pickle
import os
import io
import sys
from contextlib import contextmanager
# local imports
from settings import *
from configure_settings import *

# file that will be created for and then removed after this test has completed
test_settings_file = (os.path.join(TEST_FOLDER, "mock_settings.py"))

def generate_file_for_confset():
    """create a file for use in testing configure_settings"""

    new_lines = [
    "DISPLAY_WIDTH = 0",
    "DISPLAY_HEIGHT = 0",
    "DISPLAY_FPS = 0",
    "DISPLAY_TITLE = 'test'",
    "TILE_SIZE = 0",]

    utilities.write_file(new_lines, test_settings_file)

def test_configure_settings():
    """setup a test file, configure the settings, assert that the settings were changed"""

    generate_file_for_confset()

    inputs = io.StringIO('1024\n768\n45\ngame\n32\n')

    with replace_stdin(inputs):
        configure_settings(test_settings_file)

    try:
        with open(test_settings_file) as reader:
            file = reader.readlines()

            for line in file:
                if "DISPLAY_WIDTH" in line:
                    assert "1024" in line

                elif "DISPLAY_HEIGHT" in line:
                    assert "768" in line

                elif "DISPLAY_FPS" in line:
                    assert "45" in line

                elif "DISPLAY_TITLE" in line:
                    assert "game" in line

                elif "TILE_SIZE" in line:
                    assert "32" in line

    except Exception:
        assert True == False

    finally:
        cleanup_test_file()

def cleanup_test_file():
    """remove the testing file once the test has completed"""
    os.remove(test_settings_file)

@contextmanager
def replace_stdin(target):
    """use a context manager to change the value of sys.stdin and then revert it back"""
    orig = sys.stdin
    sys.stdin = target
    yield
    sys.stdin = orig
