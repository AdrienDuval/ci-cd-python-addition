import unittest

from addition import addition


class TestAddition(unittest.TestCase):
    def test_positive_number(self):
        self.assertEqual(addition(2, 3), 5)

    def test_zero(self):
        self.assertEqual(addition(-1, 1), 0)

    def test_avec_un_negatif(self):
        self.assertEqual(addition(-1, 1), 0)


if __name__ == '__main__':
    unittest.main()
