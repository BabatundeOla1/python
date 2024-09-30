import unittest 
import multiplicationoftwonumbers


class Testmultiplicationoftwonumbers(unittest.TestCase):

	def test_that_multiple_of_two_numbers_exist(self):
		multiplicationoftwonumbers.multiplication_of_two_numbers(1)

	'''def test_that_multiple_of_two_numbers_returns_result(self):	
		self.assertEqual(multiplicationoftwonumbers.multiplication_of_two_numbers(2, 3), 6)
		self.assertEqual(multiplicationoftwonumbers.multiplication_of_two_numbers(2, 4), 8)'''