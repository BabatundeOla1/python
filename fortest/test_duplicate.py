import unittest
import duplicate

class TestDuplicate(unittest.TestCase):
    def test_that_add_every_third_number_exist(self):
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        duplicate.add_every_third_number(numbers)

    def test_that_add_every_third_number_returns_value(self):
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        expected = 30
        self.assertEqual(duplicate.add_every_third_number(numbers), expected)


