import unittest
import returnfutureinestment2

class Testreturnfutureinestment(unittest.TestCase):

	def test_for_return_future_investment_exit(self):
		returnfutureinestment2.return_future_investment()

		
	def test_if_return_future_investment_returns_result(self):
		self.assertEqual(returnfutureinestment2.return_future_investment(1000.00, 10, 10), 100.00)