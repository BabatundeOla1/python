import unittest
import credit_card_validator


class TestIfcredit_card_validator_exist(unittest.TestCase):

	def test_that_credit_card_validator_exist(self):
		credit_card_validator.validate_credit_card(number)

	def test_that_credit_card_validator_is_negative(self):
		self.assertRaises(ValueError, credit_card_validator.validate_credit_card, (-1))






