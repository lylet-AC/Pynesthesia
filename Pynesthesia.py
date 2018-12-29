
import os
from settings import *
import configure_settings
import game_gen
from PIL import Image
import utilities

print("Welcome to Pynesthesia!")
print("For help please type 'help' \n")

EXIT = False

while EXIT == False:
    command = input("[main] Please enter a command: ")
    if command == "help":
        os.system('clear')
        print("")
        print("newgame - to create a new game")
        print("confset - configure the default game settings")
        print("helpxl - extra help for more advanced tasks")
        print("htu - how to use Pynesthesia")
        print("exit - to exit Pynesthesia")
        print("")
        print("It is recommended to first edit the settings.")
        print("")

    elif command == "newgame":
        os.system('clear')
        game_gen.create_new_game()

    elif command == "confset":
        os.system('clear')
        configure_settings.configure("settings.py")

    elif command == "helpxl":
        # TODO create additional tools for selecting specific settings configurations and add the commands to this section
        pass

    elif command == "htu":
        os.system('clear')
        print("Step 1: Place input images in the 'input' directory")
        print("These images will be converted into the game map.\n")
        print("Step 2: Place sprite images in the 'sprites' directory.")
        print("These images will take the place of each pixel in the input image.\n")
        print("Step 3: Run the confset command to configure the game settings.\n")
        print("Step 4: Run the newgame command to create a new Pynesthesia project.\n")
        print("Follow the prompts and have fun!\n")

    elif command == "exit":
        os.system('clear')
        EXIT = True

    elif command == "test":
        os.system('clear')
        INPUT_IMAGE_PATH = input(
            "\n[newgame] Please enter an image for the map: ")
        input_image = Image.open(
            os.path.join(
                MAP_INPUT_FOLDER,
                INPUT_IMAGE_PATH))

        print(utilities.get_unique_color_list(input_image))

    else:
        print("Invalid command.")
