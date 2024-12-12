import unittest
import square


class MyTestCase(unittest.TestCase):
    def test_that_number_can_be_power(self):
       self.assertEqual(square.power(2, 3), 9)

    def test_square_method(self):
        self.assertEqual(square.square(10), 100)

    def test_that_error_is_thrown_when_a_string_is_passed_as_an_argument(self):
        self.assertRaises(TypeError, square.square, "hello")

    def test_that_square_root_method(self):
        self.assertEqual(square.square_root(100), 10)

    def test_that_error_is_thrown_when_a_string_is_passed_to_squareroot(self):
        self.assertRaises(TypeError, square.square_root, "hello")

    def test_that_get_maximum_returns_the_maximum_value(self):
        self.assertEqual(square.get_maximum(1, 2, 4), 4)


if __name__ == '__main__':
    unittest.main()
