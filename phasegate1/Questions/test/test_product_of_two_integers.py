import unittest 
import product_of_two_integers


class Testmultiplicationofnumbers(unittest.TestCase):

	def test_product_of_two_integers_exist(self):
		product_of_two_integers.get_product(1, 2)

	def test_product_of_two_integers__returns_result(self):	
		self.assertEqual(product_of_two_integers.get_product(2, 3), 6)
		self.assertEqual(product_of_two_integers.get_product(2, 4), 8)

	def test_if_product_of_two_integers_returns_zero_input(self):
		self.assertEqual(product_of_two_integers.get_product(0, 0), 0)

	'''def test_if_product_of_two_integers_raises_erro_with_string_value(self):
		self.assertRaises(TypeError, product_of_two_integers.get_product, "Babs")

	def test_if_product_of_two_integers_raises_negative_value(self):
		self.assertRaises(ValueError, product_of_two_integers.get_product, "23", "15")'''