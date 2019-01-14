# Pynesthesia

Pynesthesia is a code generation tool that allows a user to draw a simple tile-based game map by using an input image.  This program then converts that input image to Pygame code with each pixel color prompting the user for some input for creating a class for the tile.  The two most important pieces of information the user will input for each detected color will be the class name, as well as an image for the tile when displayed in the game.  Pynesthesia is written in Python and outputs Python Pygame code.  The code that is output is set up to be easily modified by the user to create a game.

## Installation

Pynesthesia is a program written in Python 3.  Pip3 is the default package installer that comes with python and therefore, it is required to install other dependencies for this program.  For a step-by-step guide on installing pip3, there is a link [here](https://pip.pypa.io/en/stable/installing/).

If you do not have tkinter installed on your computer, use the following command for ubuntu to set it up:
`sudo apt-get install python-tk`

If you are on windows and need to install python3/tkinter, [download](https://www.python.org/downloads/windows/) the python3 installation file.  Ensure upon installing you check the td/tk and IDLE box for installing tkinter with python.

After installing pip3, run the following commands in the root directory of this project:

`pip3 install --upgrade pip`  
`pip3 install --user -r requirements.txt`

Afterwards, run the program using the either of the following lines depending on your python installation:
`python3 Pynesthesia.py`  
`py -3 Pynesthesia.py`

## Using Pynesthesia

Using Pynesthesia is as easy as following the on screen prompts that show up on the screen.  These prompts are set up as a Read-Eval-Print_Loop or REPL.  In REPL functionality, the main design feature is command driven actions.  This means that Pynesthesia has a set of known commands that correspond to different features of the program.  When first starting Pynesthesia, it mentions that a new user may want to type `help`.  If the user types `help` then a list of commands are printed.

 These commands are as follows:
 - `help` - prints a list of commands
 - `newgame` - follow the prompts to create a new Pygame game
 - `confset` - configure the default game settings
 - `addmap` - follow the prompts to add a map to an existing Pynesthesia game
 - `howto` - a detailed description of how to use Pynesthesia

### Important Information

Pynesthesia expects a couple things from the user in order to achieve it's goal.  First, Pynesthesia expects the input image which will become the map to be located in the `input` directory; and all images that will be used for the in game tiles to be located in the `sprites` directory.  When attempting to access an image that doesn't exist, Pynesthesia will prompt the user that the image does not exist and print out the directory it expects the image to be in.  This mostly effects the `newgame` and `addmap` commands.

Secondly, Pynesthesia generates the Pygame code in a directory specified as the GAME_TITLE.  The GAME_TITLE is gathered as user input. The user is free to remove their created game from the output directory, however, to use features such as `addmap` the created game directory must be placed back in the output directory.  This also means that certain things cannot be renamed or else Pynesthesia will not be able to edit files appropriately.  Therefore, the user should not rename or remove generated folders, python files, or remove or rename comments in the generated code.
