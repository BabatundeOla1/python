import unittest
import swap


class TestSwap(unittest.TestCase):

	def test_for_swap_function_exist(self):
		swap.get_swap([1, 2, 3, 4, 5, 6]) 
		
	def test_get_swap(self):
		array =[1, 2, 3, 4, 5, 6]
		expected = [2, 1, 4, 3, 6, 5]
		self.assertEqual(swap.get_swap(array), expected)