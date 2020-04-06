import unittest
from solution import has_cycle

class PublicTests(unittest.TestCase):
    def setUp(self):
        pass

    def test1(self):
        self.assertTrue(has_cycle([[1, 3], [0, 2], [1, 3], [0, 2]]))

    def test2(self):
        self.assertFalse(has_cycle([[1], [0, 2], [1, 3], [2]]))

    def test3(self):
        self.assertTrue(has_cycle([[1], [0, 2, 3], [1, 3], [1, 2]]))

    def test4(self):
        self.assertFalse(has_cycle([[1], [0], []]))

if __name__ == "__main__":
    unittest.main()
