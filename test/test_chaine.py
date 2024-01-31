import unittest
from chaine import miroir


class MyTestCase(unittest.TestCase):

    def test_miroir(self):
        # Test chaîne normale
        self.assertEqual(miroir("Hello"), "olleH")

        # Test chaîne vide
        self.assertEqual(miroir(""), "")

        # Test chaîne contenant des espaces
        self.assertEqual(miroir("Python is fun"), "nuf si nohtyP")

        # Test chaîne contenant des caractères spéciaux
        self.assertEqual(miroir("!@#$%"), "%$#@!")

    def test_palindrome(self):
        #Test d'un palindrome
        self.assertEqual(palindrome("racecar"), "racecar Bien dit")

        # Test d'un non-palindrome
        self.assertEqual(palindrome("hello"), "hello")

        # Test d'une chaîne vide
        self.assertEqual(palindrome(""), "")




if __name__ == '__main__':
    unittest.main()
