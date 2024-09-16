import unittest
import futureinvestmentvalue

class TestFutureInvestmentValue(unittest.TestCase):

	def test_if_future_investment_value_exit(self):
		futureinvestmentvalue.future_investment_value(1000, 10, 2)

	def test_if_future_investment_value_returns_future_investment_value(self):
		self.assertEqual(futureinvestmentvalue.future_investment_value(1000, 10, 2), 1220.39)
		self.assertEqual(futureinvestmentvalue.future_investment_value(500, 50, 3), 2173.73)

	def test_if_future_investment_value_function_raise_error_with_negative_value(self):
		self.assertRaises(ValueError, futureinvestmentvalue.future_investment_value, -1, -5, -1)

	def test_if_future_investment_value_function_raise_error_with_string_value(self):
		self.assertRaises(TypeError, futureinvestmentvalue.future_investment_value, "-1", "-5", "-1")

	def test_if_future_investment_value_handles_float_value(self):
		self.assertEqual(futureinvestmentvalue.future_investment_value(1000.5, 10.2, 2.2), 1251.01)

	def test_if_future_investment_value_function_raise_error_with_zero_input(self):
		self.assertEqual(futureinvestmentvalue.future_investment_value(0, 0, 0), 0)