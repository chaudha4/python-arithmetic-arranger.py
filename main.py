
# https://github.com/wilfredinni/python-cheatsheet

# This entrypoint file to be used in development. Start by reading README.md

import os
import sys

from unittest import main



# Execute only if running in main scope and not when running under a separate module (via import)
if __name__ == "__main__":
    # Run unit tests automatically
    seperator = "-" * 40    # You can multiply string with a int !!
    print(seperator)
    # f-Strings - New way to format strings
    info = f'Run Type[{__name__}]{"-" * 10}Package Name[{__package__}]'
    print(info)
    
    # Add src and test directory to package search path.
    appdir = os.path.abspath(os.path.join(os.path.dirname(__file__), "app"))
    arr = os.listdir(appdir)
    print(arr)

    for item in arr:
        dirName = os.path.abspath(os.path.join(os.path.dirname(__file__), "app/" + item))
        sys.path.insert(0, dirName)
        print(dirName)

    print(sys.path)

    for item in arr:
        main(module="app." + item + ".test_module", exit=False, verbosity=2)

    #main(module='app.01-arithmetic-arranger.test_module', exit=False, verbosity=2)