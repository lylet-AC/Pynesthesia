import sys
import io
import utilities
from settings import *

"""def main():
    #save the default stdin
    stdin = sys.stdin
    utilities.input = lambda _:'README.md'

    file = utilities.get_path_if_valid("test prompt", type="file", path=ROOT_FOLDER)
    # reset the input of the utilities function
    utilities.input = stdin

    print(stdin)

main()"""

from contextlib import contextmanager

@contextmanager
def replace_stdin(target):
    stdin = sys.stdin
    sys.stdin = target
    yield
    print(sys.stdin)
    sys.stdin = stdin
    print(sys.stdin)

with replace_stdin(io.StringIO("README.md")):
    file = utilities.get_path_if_valid("test prompt", type="file", path=ROOT_FOLDER)
