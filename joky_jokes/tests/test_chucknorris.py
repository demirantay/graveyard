import unittest
from jokyjokes.chucknorris import random, joke, all_jokes, jokes


# Testing Chuck Norris Module
class TestChuckNorris(unittest.TestCase):
    def setUp(self):
        pass  # Nothing to set up yet

    def test_if_random_returned_joke_is_string(self):
        random_joke = random()
        self.assertEqual(type(random_joke), type('str'))

    def test_if_length_of_list_is_ten(self):
        list_length = len(jokes)
        self.assertEqual(list_length, 10)
