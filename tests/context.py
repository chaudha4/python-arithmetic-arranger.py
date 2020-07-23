# See https://docs.python-guide.org/writing/structure/

import os
import sys

# Add src directory to package search path.
cwd = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', "src"))
sys.path.insert(0, cwd)


from arithmetic_arranger import arithmetic_arranger

if __name__ == "__main__":
    print(cwd)
    print(sys.path)
    print(arithmetic_arranger(["235 * 52"]))