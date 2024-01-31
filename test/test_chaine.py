import unittest
from miroir import miroir


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


if __name__ == '__main__':
    unittest.main()
