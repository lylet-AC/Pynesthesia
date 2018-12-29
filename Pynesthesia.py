
import os
from settings import *
import configure_settings
import gamegen

print("Welcome to Pynesthesia!")
print("For help please type 'help' \n")

EXIT = False

while EXIT == False:
    command = input("[main] Please enter a command: ")
    if command == "help":
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
        gamegen.create_new()

    elif command == "confset":
        os.system('clear')
        configure_settings.configure("settings.py")

    elif command == "exit":
        os.system('clear')
        EXIT = True
    else:
        print("Invalid command.")
