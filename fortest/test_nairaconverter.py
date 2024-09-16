import unittest 

import nairaconverter

class TestNairaConverter(unittest.TestCase):

	def test_if_naira_converter_exist(self):
		nairaconverter.naira_converter(2345)
	
	def test_if_naira_converter_returns_equal_value(self):
		self.assertEqual(nairaconverter.naira_converter(1500), 2_325_000)

	def test_if_naira_converter_raises_negative_value(self):
		self.assertRaises(ValueError, nairaconverter.naira_converter, -1500)

	def test_if_naira_converter_raises_string_type(self):
		self.assertRaises(TypeError, nairaconverter.naira_converter, "1500")

	def test_if_naira_converter_zero_value(self):
		self.assertEqual(nairaconverter.naira_converter(0), 0)