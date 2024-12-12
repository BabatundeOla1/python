import unittest
from account2 import Account2
from decimal import Decimal

class TestAccount2(unittest.TestCase):

    def setUp(self):
        self.babatunde = Account2("Babatunde", "09036011444", "1234")
    def test_that_account_exist(self):
        account1 = Account2("babatunde", "09036011444")
        account2 = Account2("Theezy", "09063475087")

    def test_that_pin_is_four_digit(self):
        self.assertRaises(ValueError, self.babatunde.set_pin, "123")
        self.assertRaises(ValueError, self.babatunde.set_pin, "12345")

    def test_that_pin_is_not_default_pin(self):
        self.assertRaises(ValueError, self.babatunde.set_pin, "1234")

    def test_that_phone_number_is_eleven_digit(self):
        self.babatunde.set_phone_number("09036011444")
        self.assertEqual(self.babatunde.get_phone_number(), "09036011444")

    def test_that_phone_number_starts_with_zeros(self):
        self.babatunde.set_phone_number("09036011444")
        self.assertEqual(self.babatunde.get_phone_number(), "09036011444")

    def test_that_you_can_deposit(self):
        self.babatunde.deposit(Decimal("100_000"))
        self.assertEqual(self.babatunde.get_balance(), Decimal("100_000"))

    def test_that_you_can_not_deposit_negative_amount(self):
        self.assertEqual(self.babatunde.get_balance(), Decimal("0.00"))
        self.assertRaises(ValueError, self.babatunde.deposit, (Decimal("-100_000")))
    def test_that_you_can_withdraw(self):
        self.assertEqual(self.babatunde.get_balance(), Decimal("0.00"))
        self.babatunde.withdraw(Decimal("0.00"))
        self.assertEqual(self.babatunde.get_balance(), Decimal("0.00"))

    def test_that_you_can_not_withdraw_negative_amount(self):
        self.assertEqual(self.babatunde.get_balance(), Decimal("0.00"))
        self.assertRaises(ValueError, self.babatunde.withdraw,(Decimal("-10_000")))

    def test_that_you_can_not_withdraw_more_than_balance(self):
        self.assertEqual(self.babatunde.get_balance(), Decimal("0.00"))
        self.assertRaises(ValueError, self.babatunde.withdraw, (Decimal("120_000")))
