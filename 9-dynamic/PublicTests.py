import unittest
from solution import num_bsts

class PublicTests(unittest.TestCase):
    def setUp(self):
        pass

    def test1(self):
        self.assertEqual(num_bsts(2), 2)

    def test2(self):
        self.assertEqual(num_bsts(40), 2622127042276492108820)

    def test3(self):
        self.assertEqual(num_bsts(20), 6564120420)

    def test4(self):
        self.assertEqual(num_bsts(100), 896519947090131496687170070074100632420837521538745909320)

if __name__ == "__main__":
    unittest.main()
