import unittest 
import onlyfloat

class TestOnlyFloat(unittest.TestCase):

	def test_if_only_float_function_exist(self):
		onlyfloat.only_float(2, 3)

	def test_if_only_float_function_returns_price(self):
		self.assertEqual(onlyfloat.only_float(150, 15), 127.5)
		self.assertEqual(onlyfloat.only_float(1500, 15), 1275)

	def test_if_only_float_function_raises_negative_value(self):
		self.assertRaises(ValueError, onlyfloat.only_float, -150, -15)

	def test_if_only_float_function_returns_zero_input(self):
		self.assertEqual(onlyfloat.only_float(0, 0), 0)

	def test_if_only_float_function_raises_error_with_string_value(self):
		self.assertRaises(TypeError, onlyfloat.only_float, "23", "15")