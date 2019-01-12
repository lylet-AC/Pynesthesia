
import os
from PIL import Image
# local imports
from settings import *
import configure_settings
import game_gen
import utilities


if __name__ == "__main__":

    # initial display messages when starting up
    print("Welcome to Pynesthesia!")
    print("For help please type 'help' \n")

    command = ""

    # begin REPL functionality
    while command != "exit":
        command = input("[main] Please enter a command: ")
        if command == "help":
            os.system('clear')
            print("")
            print("newgame - to create a new game")
            print("confset - configure the default game settings")
            print("addmap - add a map to an existing game")
            print("htu - how to use Pynesthesia")
            print("exit - to exit Pynesthesia")
            print("")
            print("It is recommended to first edit the setting.")
            print("")

        elif command == "newgame":
            os.system('clear')
            game_gen.create_new_game()

        elif command == "confset":
            os.system('clear')
            configure_settings.configure_settings("settings.py")

        elif command == "addmap":
            os.system('clear')
            game_gen.add_map_to_project()

        elif command == "htu":
            os.system('clear')
            print("Step 1: Place input images in the 'input' directory")
            print("These images will be converted into the game map.\n")
            print("Step 2: Place sprite images in the 'sprites' directory.")
            print("These images will take the place of each pixel in the input image.\n")
            print("Step 3: Run the confset command to configure the game settings.\n")
            print("Step 4: Run the newgame command to create a new Pynesthesia project.\n")
            print("Follow the prompts and have fun!\n")

        else:
            print("Invalid command.")

    os.system('clear')
