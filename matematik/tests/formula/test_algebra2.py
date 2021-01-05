import unittest
from matematik.formula.algebra2 import vertex, standart, axis_symetry
from matematik.formula.algebra2 import sum_of_cubes, different_of_cubes, cube


class Test_Vertes(unittest.TestCase):
    '''
    testing function: vertex()
    '''

    def test_if_function_returns_a_true_value(self):
        self.assertEqual(vertex(1, 2, 3, 4), 5)


class Test_Standart(unittest.TestCase):
    '''
    testing function: standart()
    '''

    def test_if_function_returns_a_true_value(self):
        self.assertEqual(standart(1, 2, 3, 4), 9)


class Test_AxisSymetry(unittest.TestCase):
    '''
    testing function: axis_symetry()
    '''

    def test_if_function_returns_a_true_value(self):
        self.assertEqual(axis_symetry(2, 4), -1)


class Test_DifferentOfCubes(unittest.TestCase):
    '''
    testing funton: different_of_cubes()
    '''

    def test_if_function_returns_a_true_value(self):
        self.assertEqual(different_of_cubes(1, 2), -7)


class Test_Cube(unittest.TestCase):
    '''
    testing function: cube()
    '''

    def test_if_function_returns_a_true_value(self):
        self.assertEqual(cube(2), 8)
