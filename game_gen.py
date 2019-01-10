from PIL import Image
import os
from settings import *
import utilities
from shutil import copy2, copytree
import pickle


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

    DEFAULT_MAP_TITLE = input("[addmap] Please enter a title for your new map: ")

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


    # define the name of the directory to be created
    NEW_GAME_FOLDER = os.path.join(OUTPUT_FOLDER, GAME_TITLE)
    LEVELS_FOLDER = os.path.join(NEW_GAME_FOLDER, "levels")

    # try to make directories, copy files, and write data
    try:
        pass
        os.mkdir(NEW_GAME_FOLDER)
        os.mkdir(LEVELS_FOLDER)
        copy_necessary_files(NEW_GAME_FOLDER)
        create_map(LEVELS_FOLDER, input_image, DEFAULT_MAP_TITLE)
        create_pygame_classes(GAME_TITLE, NEW_GAME_FOLDER, color_dict)
        create_main_game_code(GAME_TITLE, NEW_GAME_FOLDER, color_dict, DEFAULT_MAP_TITLE)
        set_unique_colors_list(LEVELS_FOLDER, unique_color_list)

    # if we encounter an exception print a failure message.
    except:
        print ("[newgame] Creation of the new game at: \n{} has failed".format(NEW_GAME_FOLDER))

    # if we did not encounter an error, print that it was successfully created
    else:
        print ("[newgame] Successfully created the new game at:\n{} ".format(NEW_GAME_FOLDER))


def copy_necessary_files(NEW_GAME_FOLDER):
    """This method will copy important files to the new game directory"""

    # copy settings.py to the new game folder
    copy2("settings.py", NEW_GAME_FOLDER)
    #copy the everything in our current SPRITE_FOLDER to a new sprites directory in the new game
    copytree(SPRITE_FOLDER, os.path.join(NEW_GAME_FOLDER, "sprites"))


def set_unique_colors_list(LEVELS_FOLDER, unique_color_list):
    """This method will dump the unique colors list into the levels directory of a game"""

    # place this list into the levels folder of an outputed game
    PICKLE_FILE = os.path.join(LEVELS_FOLDER, "color_list.p")
    # pickle lets us dump this dataset into a file
    pickle.dump(unique_color_list, open(PICKLE_FILE, "wb"))


def get_existing_color_list(LEVELS_FOLDER):
    """This method will retrieve the list of unique colors from the levels directory of a game"""

    # declare the file we would like to load
    PICKLE_FILE = os.path.join(LEVELS_FOLDER, "color_list.p")
    # load the file using pickle
    unique_color_list = pickle.load(open(PICKLE_FILE, "rb"))

    return unique_color_list


def create_pygame_classes(GAME_TITLE, NEW_GAME_FOLDER, color_dict):
    """This method will create pygame classes for each dictionary object"""

    print("[newgame] Creating PyGame classes...")

    # new_lines contains the data we will be writing to the output folder
    new_lines = ["import pygame as pg\n", "from settings import *\n"]

    # append data to new_lines.  This data is gathered from the color_dict.
    for color in color_dict:
        new_lines.append("\n")
        new_lines.append("class {}(pg.sprite.Sprite):\n".format(color_dict[color][0]))
        new_lines.append("    def __init__(self, game, x, y):\n")
        new_lines.append("        self.groups = game.background_sprites\n")
        new_lines.append("        pg.sprite.Sprite.__init__(self, self.groups)\n")
        new_lines.append("        self.game = game\n")
        new_lines.append("        self.image = game.{}_img\n".format(color_dict[color][0]))
        new_lines.append("        self.rect = self.image.get_rect()\n")
        new_lines.append("        self.x = x\n")
        new_lines.append("        self.y = y\n")
        new_lines.append("        self.rect.x = x * TILE_SIZE\n")
        new_lines.append("        self.rect.y = y * TILE_SIZE\n")

    # declare a file in our new game called "classes.py"
    CLASS_FILE = os.path.join(NEW_GAME_FOLDER, "classes.py")
    # write the content of new_lines to the CLASS_FILE
    utilities.write_file(new_lines, CLASS_FILE)

def create_map(LEVELS_FOLDER, input_image, MAP_TITLE):
    """This method will save the map for the input level into the levels directory of the new game"""

    # this dataset is a list of lists that contains the map data based on the input image
    # this dataset is formatted with each row of pixels being it's own list
    map_list = utilities.get_color_map_list(input_image)

    # much like before we set up a file to dump our dataset
    # this file is named after whatever the user of Pynesthesia set MAP_TITLE to
    PICKLE_FILE = os.path.join(LEVELS_FOLDER, "{}.p".format(MAP_TITLE))
    pickle.dump(map_list, open(PICKLE_FILE, "wb"))


def add_map_to_project():
    """This method adds a new map to an existing game"""

    # new_lines contains data to be written to a file
    new_lines = []
    # set up our color dictionary which will be added too shortly
    color_dict = {}

    # the user will input some names for the existing project and name their new map
    GAME_TITLE = input("[addmap] Please enter the name of your project: ")
    MAP_TITLE = input("[addmap] Please enter a title for your new map: ")

    # based on the GAME_TITLE we find the other needed directories
    GAME_FOLDER = os.path.join(OUTPUT_FOLDER, GAME_TITLE)
    GAME_FILE = os.path.join(GAME_FOLDER, GAME_TITLE + ".py")
    CLASS_FILE = os.path.join(GAME_FOLDER, "classes.py")
    LEVELS_FOLDER = os.path.join(GAME_FOLDER, "levels")

    # exit defaults to false
    EXIT = False

    # iterate through the while loop until correct input is gathered
    while EXIT == False:

        # try to get the input image
        try:
            INPUT_IMAGE_PATH = input(
                "\n[addmap] Please enter an image for the map: ")
            input_image = Image.open(os.path.join(MAP_INPUT_FOLDER, INPUT_IMAGE_PATH))

            EXIT = True

        # if bad input is entered, an exception is thrown and caught here
        except BaseException:
            print("[addmap] This image is not a supported format or does not exist.")
            print("[addmap] Please insert the image into the 'sprites' directory and try again.\n")

    # based on the gathered input we can create the map
    create_map(LEVELS_FOLDER, input_image, MAP_TITLE)

    # next we need to check if the new map contains a new color.
    old_colors = get_existing_color_list(LEVELS_FOLDER)
    new_colors = utilities.get_unique_color_list(input_image)

    # the utilities function for getting an updated color list returns three values.
    # these values are an updated color list, a boolean flag which tells us if a new color was found, as well as a list of new colors.
    updated_unique_color_list, new_tile_flag, new_colors = utilities.return_updated_list(old_colors, new_colors)

    # in this game we then update the dumped list of unique colors incase we need to use it again
    set_unique_colors_list(LEVELS_FOLDER, updated_unique_color_list)

    # if we did find a new color, we need to create game code for it
    if new_tile_flag:
        for color in new_colors:
            os.system('clear')
            object_name = input(
                "[newgame] What would you like color {} to represent? ".format(color))

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

                    #create the color dictionary using user input
                    color_dict[color] = [object_name, object_image_path]

                    EXIT = True

                # if bad input is entered, an exception is thrown and caught here
                except BaseException:
                    print(
                        "[newgame] This image is not a supported format or does not exist.")
                    print(
                        "[newgame] Please insert the image into the 'sprites' directory and try again.\n")

        # attempt to update the classes.py file with new_lines based on the color_dict
        try:
            print("[addmap] Loading the file: ", CLASS_FILE, "...\n")

            with open(CLASS_FILE) as reader:
                file = reader.readlines()

                for line in file:
                    # add all the pre-existing lines to new_lines
                    new_lines.append(line)

                    # if we find "load_data(self):" add the line of code that loads the new map
                    if "from settings import *" in line:
                        for color in color_dict:
                            new_lines.append("\n")
                            new_lines.append("class {}(pg.sprite.Sprite):\n".format(color_dict[color][0]))
                            new_lines.append("    def __init__(self, game, x, y):\n")
                            new_lines.append("        self.groups = game.background_sprites\n")
                            new_lines.append("        pg.sprite.Sprite.__init__(self, self.groups)\n")
                            new_lines.append("        self.game = game\n")
                            new_lines.append("        self.image = game.{}_img\n".format(color_dict[color][0]))
                            new_lines.append("        self.rect = self.image.get_rect()\n")
                            new_lines.append("        self.x = x\n")
                            new_lines.append("        self.y = y\n")
                            new_lines.append("        self.rect.x = x * TILE_SIZE\n")
                            new_lines.append("        self.rect.y = y * TILE_SIZE\n")

        # if we cannot update the file, the exception is caught and an error message is returned
        except IOError:
            print(
                "\n[addmap] An IOError occured.  Perhaps the game file has been renamed or removed.\n")

        # write to the class file and then dump new_lines
        utilities.write_file(new_lines, CLASS_FILE)
        reader.close()
        new_lines = []

    # regardless of a new color, the GAME_FILE needs updated.  This also uses color_dict.
    try:
        print("[addmap] Loading the file: ", GAME_FILE, "...\n")

        with open(GAME_FILE) as reader:
            file = reader.readlines()

            for line in file:
                # add all the pre-existing lines to new_lines
                new_lines.append(line)

                # if we find "# load the map data", we can write the line of code that loads the new map beneath this comment
                if "        # load the map data" in line:
                    #line = line.replace("\n", "")
                    new_lines.append("        self.{}_map = pickle.load(open(os.path.join(LEVELS_FOLDER, \"{}.p\"), \"rb\"))\n".format(MAP_TITLE, MAP_TITLE))

                # if we find "# load the image data", we can write the lines of code that load the image beneath this comment
                if "        # load the image data" in line and new_tile_flag:
                    for color in color_dict:
                        new_lines.append("        self.{}_img = pg.image.load(os.path.join(SPRITE_FOLDER, \"{}\"))\n".format(color_dict[color][0], color_dict[color][1]))
                        new_lines.append("        self.{}_img = pg.transform.scale(self.{}_img, (TILE_SIZE, TILE_SIZE))\n".format(color_dict[color][0], color_dict[color][0]))

                # if we find "# each color will load a specific tile", we can write the line of code that places the images in pygame beneath this comment
                if "                # each color will load a specific tile" in line and new_tile_flag:
                    for color in color_dict:
                        new_lines.append("                if color == {}:\n".format(color))
                        new_lines.append("                    {}(self, col, row)\n".format(color_dict[color][0]))

    # if anything went wrong, the exception is caught and an error message is printed
    except IOError:
        print(
            "\n[addmap] An IOError occured.  Perhaps the game file has been renamed or removed.\n")


    # write the new lines and then close the reader
    utilities.write_file(new_lines, GAME_FILE)
    reader.close()


def create_main_game_code(GAME_TITLE, NEW_GAME_FOLDER, color_dict, MAP_TITLE):
    """This method will create pygame code for the main game"""

    # data in new_lines will be written to a file with the GAME_TITLE inside a directory of the NEW_GAME_FOLDER
    new_lines = ["import pygame as pg\n",
    "import sys\n",
    "import pickle\n",
    "from settings import *\n",
    "from classes import *\n",
    "\n",
    "class Game:\n",
    "    def __init__(self):\n",
    "        pg.init()\n",
    "        self.screen = pg.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))\n",
    "        pg.display.set_caption(DISPLAY_TITLE)\n",
    "        self.clock = pg.time.Clock()\n",
    "        pg.key.set_repeat(1, 1)\n",
    "        self.load_data()\n",
    "        self.set_current_map(self.{}_map)\n".format(MAP_TITLE),
    "\n",
    "    def load_data(self):\n",
    "        # load the map data\n",
    "        self.{}_map = pickle.load(open(os.path.join(LEVELS_FOLDER, \"{}.p\"), \"rb\"))\n".format(MAP_TITLE, MAP_TITLE),
    "\n",
    "        # load the image data\n"]

    # iterates through the color_dict and pulls data.   Then uses .format() to place this data in a line.
    for color in color_dict:
        new_lines.append("        self.{}_img = pg.image.load(os.path.join(SPRITE_FOLDER, \"{}\"))\n".format(color_dict[color][0], color_dict[color][1]))
        new_lines.append("        self.{}_img = pg.transform.scale(self.{}_img, (TILE_SIZE, TILE_SIZE))\n".format(color_dict[color][0], color_dict[color][0]))

    new_lines.append("\n")
    new_lines.append("    def new(self):\n")
    new_lines.append("        # initialize all variables and do all the setup for a new game\n")
    new_lines.append("        self.background_sprites = pg.sprite.Group()\n")
    new_lines.append("\n")
    new_lines.append("        # logic for drawing tiles from a list of lists\n")
    new_lines.append("        for col, colors in enumerate(self.current_map):\n")
    new_lines.append("            for row, color in enumerate(colors):\n")
    new_lines.append("                # each color will load a specific tile\n")

    # iterates through the color_dict and pulls data.   Then uses .format() to place this data in a line.
    for color in color_dict:
        new_lines.append("                if color == {}:\n".format(color))
        new_lines.append("                    {}(self, col, row)\n".format(color_dict[color][0]))

    new_lines.append("\n")
    new_lines.append("    def set_current_map(self, map_data):\n")
    new_lines.append("        # TODO: use this method to change the current map\n")
    new_lines.append("        self.current_map = map_data\n")

    new_lines.append("\n")
    new_lines.append("    def run(self):\n")
    new_lines.append("        # game loop - set self.playing = False to end the game\n")
    new_lines.append("        self.playing = True\n")
    new_lines.append("        while self.playing:\n")
    new_lines.append("            self.dt = self.clock.tick(DISPLAY_FPS) / 1000\n")
    new_lines.append("            self.events()\n")
    new_lines.append("            self.update()\n")
    new_lines.append("            self.draw()\n")

    new_lines.append("\n")
    new_lines.append("    def quit(self):\n")
    new_lines.append("        pg.quit()\n")
    new_lines.append("        sys.exit()\n")

    new_lines.append("\n")
    new_lines.append("    def update(self):\n")
    new_lines.append("        # update portion of the game loop\n")
    new_lines.append("        self.background_sprites.update()\n")

    new_lines.append("\n")
    new_lines.append("    def draw(self):\n")
    new_lines.append("        self.screen.fill((0, 0, 0))\n")
    new_lines.append("        self.background_sprites.draw(self.screen)\n")
    new_lines.append("        pg.display.flip()\n")

    new_lines.append("\n")
    new_lines.append("    def events(self):\n")
    new_lines.append("        # catch all events here\n")
    new_lines.append("        pressed = pg.key.get_pressed()\n")
    new_lines.append("        for event in pg.event.get():\n")
    new_lines.append("            if event.type == pg.QUIT:\n")
    new_lines.append("                self.quit()\n")
    new_lines.append("            if event.type == pg.KEYDOWN:\n")
    new_lines.append("                if event.key == pg.K_ESCAPE:\n")
    new_lines.append("                    self.quit()\n")

    new_lines.append("\n")
    new_lines.append("g = Game()\n")
    new_lines.append("while True:\n")
    new_lines.append("    g.new()\n")
    new_lines.append("    g.run()\n")

    # now that all the pygame code is appended to new_lines, create the file and write to it
    GAME_FILE = os.path.join(NEW_GAME_FOLDER, "{}.py".format(GAME_TITLE))
    utilities.write_file(new_lines, GAME_FILE)
