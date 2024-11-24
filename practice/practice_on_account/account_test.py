import unittest
from account import Account


class MyTestCase(unittest.TestCase):

    def test_that_balance_is_equals_zero(self):
        theezy_account = Account()
        self.assertEqual(1000, theezy_account.get_balance())


    def test_that_account_can_deposit_once(self):
        theezy_account = Account()
        self.assertEqual(1000, theezy_account.get_balance())
        theezy_account.make_deposit(500)
        self.assertEqual(1500, theezy_account.get_balance())

    def test_that_you_can_deposit_twice(self):
        theezy_account = Account()
        self.assertEqual(1000, theezy_account.get_balance())
        theezy_account.make_deposit(1_000)
        theezy_account.make_deposit(1_000)
        self.assertEqual(3000, theezy_account.get_balance())

    def test_that_you_cant_deposit_amount_less_than_one(self):
        theezy_account = Account()
        self.assertEqual(1000, theezy_account.get_balance())
        theezy_account.make_deposit(-50)
        self.assertRaises(ValueError)

    def test_that_you_can_withdraw(self):
        theezy_account = Account()
        self.assertEqual(1000, theezy_account.get_balance())
        theezy_account.make_withdraw(500)
        self.assertEqual(500, theezy_account.get_balance())

    # def test_that_you_can_withdraw(self):
    #     theezy_account = Account()
    #     self.assertEqual(1000, theezy_account.get_balance())
    #     theezy_account.make_withdraw(1100)
    #     self.assertRaises(ValueError)


