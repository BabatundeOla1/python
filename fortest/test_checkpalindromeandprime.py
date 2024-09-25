import unittest 
import checkpalindromeandprime

class TestCheckPalindromeAndPrime(unittest.TestCase):

	def test_if_check_palindrome_and_check_prime_exist(self):
		checkpalindromeandprime.check_palindrome(121)
		checkpalindromeandprime.check_prime(121)


