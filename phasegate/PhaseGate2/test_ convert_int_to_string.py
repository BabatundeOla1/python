import unittest 
import convert_int_to_string


class TestConvertIntToString(unittest.TestCase):
	
	def test_for_string_to_int_function_exist(self):
		convert_int_to_string.string_to_int(1, 2)

	def test_that_string_to_int_returns_value(self):
		self.assertEqual(convert_int_to_string.string_to_int("3", "4"), "7")

	def test_that_string_to_int_returns_error_with_negative_value(self):
		self.assertRaises(ValueError, convert_int_to_string.string_to_int, ("-3", "-4"))