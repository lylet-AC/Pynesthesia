from PIL import Image
import os
from settings import *
import utilities


def create_new_game():

    # define a dictionary to store colors and their associated sprites and
    # class names
    color_dict = {}

    # the title of the game project.  This will later turn into the directory
    # of the generated code.
    GAME_TITLE = input("[newgame] Please enter a name for your project: ")

    # exit defaults to false
    EXIT = False

    # iterate through the while loop until correct input is gathered
    while EXIT == False:

        # try to get the input image
        try:
            INPUT_IMAGE_PATH = input(
                "\n[newgame] Please enter an image for the map: ")
            input_image = Image.open(
                os.path.join(
                    MAP_INPUT_FOLDER,
                    INPUT_IMAGE_PATH))
            EXIT = True

        # if bad input is entered, an exception is thrown and caught here
        except BaseException:
            print("[newgame] This image is not a supported format or does not exist.")
            print(
                "[newgame] Please insert the image into the 'sprites' directory and try again.\n")

    # gather the list of unique colors from the input image
    unique_color_list = utilities.get_unique_color_list(input_image)

    # for each color in the list we ask the user to enter a class name and
    # sprite image
    for color in unique_color_list:
        os.system('clear')
        object_name = input(
            "[newgame] What would you like color {} to represent? ".format(color))

        # exit is false as default
        EXIT = False

        # iterate through the while loop until correct input is gathered
        while EXIT == False:

            # try to get the sprite image
            try:
                object_image_path = input(
                    "\n[newgame] Please provide the image for this object: ")
                test_open = Image.open(
                    os.path.join(
                        SPRITE_FOLDER,
                        object_image_path))

                color_dict[color] = [object_name, object_image_path]

                EXIT = True

            # if bad input is entered, an exception is thrown and caught here
            except BaseException:
                print(
                    "[newgame] This image is not a supported format or does not exist.")
                print(
                    "[newgame] Please insert the image into the 'sprites' directory and try again.\n")

    os.system('clear')
    create_pygame_classes(GAME_TITLE, unique_color_list, color_dict)


def create_pygame_classes(GAME_TITLE, unique_color_list, color_dict):
    """This method will create pygame classes for each dictionary object"""

    # define the name of the directory to be created
    NEW_GAME_FOLDER = os.path.join(OUTPUT_FOLDER, GAME_TITLE)

    try:
        pass
        os.mkdir(NEW_GAME_FOLDER)
    except OSError:
        print ("[newgame] Creation of the new game directory at: \n{} has failed".format(NEW_GAME_FOLDER))
    else:
        print ("[newgame] Successfully created the new game directory at:\n{} ".format(NEW_GAME_FOLDER))


    print("[newgame] Creating PyGame classes...")

    new_lines = ["import pygame as pg\n", "from settings import *"]


    for color in color_dict:
        new_lines.append("\n")
        new_lines.append("class {}(pg.sprite.Sprite):\n".format(color_dict[color][0]))
        new_lines.append("    def __init__(self, game, x, y):\n")
        new_lines.append("        self.groups = game.all_sprites\n")
        new_lines.append("        pg.sprite.Sprite.__init__(self, self.groups)\n")
        new_lines.append("        self.game = game\n")
        new_lines.append("        self.image = game.{}\n".format(color_dict[color][1]))
        new_lines.append("        self.rect = self.image.get_rect()\n")
        new_lines.append("        self.x = x\n")
        new_lines.append("        self.y = y\n")

    CLASS_FILE = os.path.join(NEW_GAME_FOLDER, "classes.py")
    utilities.write_file(new_lines, CLASS_FILE)
