
# https://github.com/wilfredinni/python-cheatsheet

# This entrypoint file to be used in development. Start by reading README.md

import os
import sys

from unittest import main

# Add src and test directory to package search path.
srcdir = os.path.abspath(os.path.join(os.path.dirname(__file__), "src"))
tstdir = os.path.abspath(os.path.join(os.path.dirname(__file__), "tests"))
sys.path.insert(0, srcdir)
sys.path.insert(0, tstdir)


# Execute only if running in main scope and not when running under a separate module (via import)
if __name__ == "__main__":
    # Run unit tests automatically
    main(module='test_arithmetic_arranger', exit=False, verbosity=2)