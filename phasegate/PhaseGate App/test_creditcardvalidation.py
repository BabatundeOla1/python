import unittest
import creditcardvalidation

class TestCreditCardValidatio(unittest.TestCase):
	
	def test_if_creditcard_validation_exist(self):
		creditcardvalidation.validate_card("5199110824684028")
		creditcardvalidation.check_validity("5199110824684028")

	def test_that_creditcard_validation_returns_result(self):
		self.assertEqual(creditcardvalidation.validate_card("5199110824684028"), "MasterCard")
		self.assertEqual(creditcardvalidation.check_validity("5199110824684028"), "Valid")

	def test_creditcard_validation_raises_error_for_string_with_non_digits(self):
		self.assertRaises(TypeError, creditcardvalidation.validate_card("51991108axd24684028"))
		self.assertRaises(TypeError, creditcardvalidation.check_validity("51991108axd24684028"))
	

	def test_if_creditcard_validation_raises_error_for_float_value(self):
		self.assertRaises(TypeError, creditcardvalidation.validate_card("51.99110824684028"))
		self.assertRaises(TypeError, creditcardvalidation.check_validity("51.99110824684028"))
