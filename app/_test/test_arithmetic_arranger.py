import unittest

# This import not required since it is already in __init__.py
# from app.arithmetic_arranger import arithmetic_arranger

# A testcase is created by subclassing unittest.TestCase. 
# 
# The three individual tests are defined with methods whose names start with the letters test. 
# This naming convention informs the test runner about which methods represent tests. 
# 
# The crux of each test  is a call to assertEqual() to check for an expected result; assertTrue() 
# or assertFalse() to verify a condition; or assertRaises() 
# to verify that a specific exception gets raised. These methods are used instead of the 
# assert statement so the test runner can # accumulate all test results and produce a report. 
# 
# The setUp() and tearDown() methods allow you to define instructions that will 
# be executed before and after each test method.

from app.arithmetic_arranger import arithmetic_arranger

class UnitTests(unittest.TestCase):
    def test_simple_arangement(self):
        actual = arithmetic_arranger(["235 + 52"])
        expected = "  235\n+  52\n-----"
        self.assertEqual(actual, expected)    
        
    def test_arrangement(self):
        actual = arithmetic_arranger(["3 + 855", "3801 - 2", "45 + 43", "123 + 49"])
        expected = "    3      3801      45      123\n+ 855    -    2    + 43    +  49\n-----    ------    ----    -----"
        self.assertEqual(actual, expected, 'Expected different output when calling "arithmetic_arranger()" with ["3 + 855", "3801 - 2", "45 + 43", "123 + 49"]')

        actual = arithmetic_arranger(["11 + 4", "3801 - 2999", "1 + 2", "123 + 49", "1 - 9380"])
        expected = "  11      3801      1      123         1\n+  4    - 2999    + 2    +  49    - 9380\n----    ------    ---    -----    ------"
        self.assertEqual(actual, expected, 'Expected different output when calling "arithmetic_arranger()" with ["11 + 4", "3801 - 2999", "1 + 2", "123 + 49", "1 - 9380"]')

    def test_too_many_problems(self):
        actual = arithmetic_arranger(["44 + 815", "909 - 2", "45 + 43", "123 + 49", "888 + 40", "653 + 87"])
        expected = "Error: Too many problems."
        self.assertEqual(actual, expected, 'Expected calling "arithmetic_arranger()" with more than five problems to return "Error: Too many problems."')

    def test_incorrect_operator(self):
        actual = arithmetic_arranger(["3 / 855", "3801 - 2", "45 + 43", "123 + 49"])
        expected = "Error: Operator must be '+' or '-'."
        self.assertEqual(actual, expected, '''Expected calling "arithmetic_arranger()" with a problem that uses the "/" operator to return "Error: Operator must be '+' or '-'."''')
        
    def test_too_many_digits(self):
        actual = arithmetic_arranger(["24 + 85215", "3801 - 2", "45 + 43", "123 + 49"])
        expected = "Error: Numbers cannot be more than four digits."
        self.assertEqual(actual, expected, 'Expected calling "arithmetic_arranger()" with a problem that has a number over 4 digits long to return "Error: Numbers cannot be more than four digits."')

    def test_only_digits(self):
        actual = arithmetic_arranger(["98 + 3g5", "3801 - 2", "45 + 43", "123 + 49"])
        expected = "Error: Numbers must only contain digits."
        self.assertEqual(actual, expected, 'Expected calling "arithmetic_arranger()" with a problem that contains a letter character in the number to return "Error: Numbers must only contain digits."')

    def test_solutions(self):
        actual = arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49"], True)
        expected = "   32         1      45      123\n- 698    - 3801    + 43    +  49\n-----    ------    ----    -----\n -666     -3800      88      172"
        self.assertEqual(actual, expected, 'Expected solutions to be correctly displayed in output when calling "arithmetic_arranger()" with arithemetic problems and a second argument of `True`.')


# Execute only if running in main scope and not when running under a separate module (via import)
if __name__ == "__main__":
    mesg = "\nExecuting module as script not allowed\nPlease run main.py from root folder\n"
    print(f'\n\n{"-"*len(mesg)}{mesg}{"-"*40}\n')
    #unittest.main(verbosity=2)