import unittest
from solution import num_bsts

class PublicTests(unittest.TestCase):
    def setUp(self):
        pass

    def test1(self):
        self.assertEqual(num_bsts(2), 2)

    def test2(self):
        self.assertEqual(num_bsts(3), 5)

    def test3(self):
        self.assertEqual(num_bsts(5), 42)

    def test4(self):
        self.assertEqual(num_bsts(4), 14)

if __name__ == "__main__":
    unittest.main()
