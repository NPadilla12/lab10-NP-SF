# https://github.com/NPadilla12/lab10-NP-SF
# Partner 1: Nicholas Padilla
# Partner 2: Sayyed Faisal


import unittest
from calculator import *

class TestCalculator(unittest.TestCase):

    ######### Partner 2

    def test_add(self): # 3 assertions
        self.assertEqual(add(1, 1), 2)
        self.assertEqual(add(500, 501), 1001)
        self.assertEqual(add(123, 456), 579)


    def test_subtract(self): # 3 assertions
        self.assertEqual(subtract(10, 3), 7)
        self.assertEqual(subtract(0, 23), -23)
        self.assertEqual(subtract(-57, 13), -70)


    ######## Partner 1

    # def test_multiply(self): # 3 assertions
    #     fill in code


    # def test_divide(self): # 3 assertions
    #     fill in code
    # ##########################


    ######## Partner 2

    def test_divide_by_zero(self): # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)


    def test_logarithm(self): # 3 assertions
        self.assertEqual(logarithm(5, 1), 0)
        self.assertEqual(logarithm(10, 100), 2)
        self.assertEqual(logarithm(3, 81), 4)


    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            log(-5, 0)


    ######## Partner 1

    # def test_log_invalid_argument(self): # 1 assertion
    #     # call log function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     logarithm(0, 5)
    #     fill in code


    # def test_hypotenuse(self): # 3 assertions
    #     fill in code


    # def test_sqrt(self): # 3 assertions
    #     # Test for invalid argument, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #    square_root(NUM)
    #     # Test basic function
    #     fill in code
    ##########################


# Do not touch this
if __name__ == "__main__":
    unittest.main()