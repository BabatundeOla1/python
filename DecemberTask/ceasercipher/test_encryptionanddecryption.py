import unittest

from DecemberTask.ceasercipher import encryptionanddecryption


class MyTestCase(unittest.TestCase):
    def test_that_message_can_be_encrypted_in_uppercase(self):
        text = "CODEDAMN"
        number = 3
        self.assertEqual("FRGHGDPQ", encryptionanddecryption.encrypt(text, number))

    def test_that_messge_can_be_encrypted_in_lowercase(self):
        text = "codedamn"
        number = 3
        self.assertEqual("frghgdpq", encryptionanddecryption.encrypt(text, number))

    def test_that_error_is_thrown_when_encryption_number_is_less_than_one(self):
        text = "codedamn"
        number = -3
        with self.assertRaises(ValueError):
            encryptionanddecryption.encrypt(text, number)

    def test_that_message_can_be_decrypted_in_uppercase(self):
        text = "FRGHGDPQ"
        number = 3
        self.assertEqual("CODEDAMN", encryptionanddecryption.decrypt(text, number))

    def test_that_messge_can_be_decrypted_in_lowercase(self):
        text = "frghgdpq"
        number = 3
        self.assertEqual("codedamn", encryptionanddecryption.decrypt(text, number))

    def test_that_error_is_thrown_when_decryption_number_is_less_than_one(self):
        text = "codedamn"
        number = -3
        with self.assertRaises(ValueError):
            encryptionanddecryption.decrypt(text, number)



if __name__ == '__main__':
    unittest.main()
