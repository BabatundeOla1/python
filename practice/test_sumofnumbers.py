import unittest
import sumofnumbers

class MyTestCase(unittest.TestCase):
    def test_that_it_returns_true_when_its_a_palindrom(self):
        words = "MADAM"
        self.assertTrue(sumofnumbers.palindrom_check(words))
    def test_that_it_returns_false_when_its_not_a_palindrom(self):
        words = "MADAW"
        self.assertFalse(sumofnumbers.palindrom_check(words))



if __name__ == '__main__':
    unittest.main()
