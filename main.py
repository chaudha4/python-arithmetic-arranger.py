
# https://github.com/wilfredinni/python-cheatsheet

# This entrypoint file to be used in development. Start by reading README.md

import os
import sys

from unittest import main

info = f'Run Type[{__name__}]{"-" * 10}Package Name[{__package__}]'
print(info)

import app.arithmetic_arranger as aa
from app import arithmetic_arranger as bb
#from app import mean_var_std as cc
#from tests import test_mean_var_std as dd

import app.mean_var_std as mean_var_std


print(aa.arithmetic_arranger(["235 + 52"]))
print(bb.arithmetic_arranger(["235 + 52"]))
print(mean_var_std.calculate([2,6,2,8,4,0,1,5,7]))


# Add src and test directory to package search path.
#srcdir = os.path.abspath(os.path.join(os.path.dirname(__file__), "app"))
#tstdir = os.path.abspath(os.path.join(os.path.dirname(__file__), "tests"))
#sys.path.insert(0, srcdir)
#sys.path.insert(0, tstdir)

#main()
main(module='app._test.test_arithmetic_arranger', exit=False, verbosity=2)
main(module='tests.test_arithmetic_arranger', exit=False, verbosity=2)
main(module='tests.test_mean_var_std', exit=False, verbosity=2)
main(module='tests.test_time_calculator', exit=False, verbosity=2)


# Execute only if running in main scope and not when running under a separate module (via import)
if __name__ == "__main__":
    # Run unit tests automatically
    seperator = "-" * 40    # You can multiply string with a int !!
    print(seperator)
    # f-Strings - New way to format strings
    info = f'Run Type[{__name__}]{"-" * 10}Package Name[{__package__}]'
    print(info)
    
    #main(module='test_arithmetic_arranger', exit=False, verbosity=2)