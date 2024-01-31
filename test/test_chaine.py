import unittest
from chaine import miroir
from chaine import palindrome
from chaine import bonjour


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

    def test_bonjour(self):
        # Test d'une chaine basique
        self.assertEqual(bonjour("Ca va"), "Bonjour Ca va")

        # Test d'une chaine vide
        self.assertEqual(bonjour(""), "Bonjour ")

    def test_aurevoir(self):
        # Test d'une chaine basique
        self.assertEqual(bonjour("Bonjour"), "Bonjour Au revoir")

        # Test d'une chaine vide
        self.assertEqual(bonjour(""), " Au revoir")




if __name__ == '__main__':
    unittest.main()
