import unittest
import primeandparlindrome

class TestPrimeAndPalindrome(unittest.TestCase):

	def test_if_primeandparlindrome_function_exist(self):
		primeandparlindrome.get_prime(121)

		primeandparlindrome.get_parlindrome(121)

		primeandparlindrome.is_boolean()

	def test_that_primeandparlindrome_function_returns_result(self):
		self.assertTrue(primeandparlindrome.get_prime(121))
		self.assertFalse(primeandparlindrome.get_prime(121))

		self.assertTrue(primeandparlindrome.get_parlindrome(121))
		self.assertFalse(primeandparlindrome.get_parlindrome(120))

		#self.assertTrue(primeandparlindrome.is_boolean())
		#self.assertFalse(primeandparlindrome.is_boolean())