
# https://github.com/wilfredinni/python-cheatsheet

# This entrypoint file to be used in development. Start by reading README.md

import os
import sys

from unittest import main

def print_useless_stuff():
    # Run unit tests automatically
    seperator = "-" * 60    # You can multiply string with a int !!
    print(seperator)
    # f-Strings - New way to format strings
    info = f'Run Type[{__name__}]{"-" * 10}Package Name[{__package__}]'
    print(info)
    print(seperator)

    directories=[d for d in os.listdir(os.getcwd()) if os.path.isdir(d)]
    paths=[ os.listdir(os.path.abspath(os.path.join(os.path.dirname(__file__), d)))  for d in directories ]    
    print(paths)
 
def run_tests(dir):
    
    pkgdir = os.path.abspath(os.path.join(os.path.dirname(__file__), dir))
    subpkgs = [os.path.abspath(os.path.join(os.path.dirname(__file__), dir + "/" + m)) for m in os.listdir(pkgdir)]
    modules = [m for m in os.listdir(pkgdir)]
    for aa in subpkgs:
        sys.path.insert(0, aa)
    
    for aa in modules:        
        main(module = dir + "." + aa + ".test_module", exit=False, verbosity=1)


# Execute only if running in main scope and not when running under a separate module (via import)
if __name__ == "__main__":
   
    # Add src and test directory to package search path.

    
    run_tests("computing")
    run_tests("data_analysis")

