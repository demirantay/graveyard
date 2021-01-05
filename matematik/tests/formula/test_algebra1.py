import unittest
from matematik.formula.algebra1 import slope_intercept, point_slope, slope_formula


class Test_SlopeIntercept(unittest.TestCase):

    def test_if_the_function_returns_a_int(self):
        self.assertEqual(type(slope_intercept(4, 5, 2)), type(10))

    def test_if_the_function_returns_a_true_value(self):
        self.assertEqual(slope_intercept(1, 2, 3), 5)

    def test_if_the_function_works_with_negative_nums(self):
        self.assertEqual(slope_intercept(-1, 2, 3), 1)


class Test_PointSlope(unittest.TestCase):

    def test_if_the_function_returns_a_int(self):
        self.assertEqual(type(point_slope(5, 4, 1)), type(10))

    def test_if_the_function_returns_a_true_value(self):
        self.assertEqual(point_slope(1, 2, 1), 1)

    def test_if_the_function_works_with_negative_nums(self):
        self.assertEqual(point_slope(-1, 2, 1), -1)


class Test_SlopeFormula(unittest.TestCase):

    def test_if_the_function_returns_a_true_value(self):
        self.assertEqual(slope_formula(2, 4, 2, 4), 1)
