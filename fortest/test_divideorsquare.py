import unittest 
import divideorsquare


class TestDivideOrSquare(unittest.TestCase):

	def test_for_divide_or_square_function_exist(self):
		divideorsquare.divide_or_square(1)


	def test_that_divide_or_square_function_returns_squareroot_result(self):	
		self.assertEqual(divideorsquare.divide_or_square(100), 10)
		self.assertEqual(divideorsquare.divide_or_square(25), 5)
		self.assertEqual(divideorsquare.divide_or_square(200), 14.142135623730951)
		self.assertEqual(divideorsquare.divide_or_square(65), 8.06225774829855)

	def test_that_divide_or_square_function_return_error_with_string_value(self):	
		self.assertRaises(TypeError, divideorsquare.divide_or_square, "string")

	def test_that_divide_or_square_function_return_error_with_negative_value(self):
		self.assertRaises(ValueError, divideorsquare.divide_or_square, (-1))

	def test_that_divide_or_square_function_return_error_with_zero_input(self):
		self.assertEqual(divideorsquare.divide_or_square(0), 0)

	

	