import unittest
from matematik.formula.geometry import area_of_triangle, area_of_circle
from matematik.formula.geometry import circumfrence, area_of_rect
from matematik.formula.geometry import trapezoid_midsegment
from matematik.formula.geometry import volume_of_rect_prism, volume_of_cone
from matematik.formula.geometry import volume_of_tri_prism, volume_of_cylander
from matematik.formula.geometry import volume_of_rect_pyramid, volume_of_sphere
from matematik.formula.geometry import volume_of_tri_pyramid
from matematik.formula.geometry import volume_of_hemisphere


class Test_AreaOfTriangle(unittest.TestCase):
    '''
    tesing function: area_of_triange()
    '''

    def test_if_the_func_returns_a_true_value(self):
        self.assertEqual(area_of_triangle(2, 4), 4)


class Test_TrapezoidMidsegment(unittest.TestCase):
    '''
    testing function: trapezoid_midsegment()
    '''

    def test_if_the_func_returns_a_true_value(self):
        self.assertTrue(trapezoid_midsegment(5, 10), 7.5)


class Test_VolumeOfTriPrism(unittest.TestCase):
    '''
    testing  function: volume_of_tri_prism()
    '''

    def test_if_the_func_returns_a_true_value(self):
        self.assertEqual(volume_of_tri_prism(2, 4), 16)


# self note: I need to add more tests to this module. Atm i do not have time
