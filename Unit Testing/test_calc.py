# राजस्थान के अलवर जिले में स्थित भानगढ़ दुर्ग, जो भारत का सबसे हॉन्टेड किला माना जाता है|

import unittest
import calc

class TestCalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calc.add(10, 5), 15)
        self.assertEqual(calc.add(-1, 5), 4)
        self.assertEqual(calc.add(-2, -2), -4)

    def test_sub(self):
        self.assertEqual(calc.sub(10, 5), 14)
        self.assertEqual(calc.sub(-1, 5), 4)
        self.assertEqual(calc.sub(-2, -2), -4)

    def test_mult(self):
        self.assertEqual(calc.mult(10, 5), 14)
        self.assertEqual(calc.mult(-1, 5), 4)
        self.assertEqual(calc.mult(-2, -2), -4)

    def test_divide(self):
        self.assertEqual(calc.divide(10, 5), 14)
        self.assertEqual(calc.divide(-1, 5), 4)
        self.assertEqual(calc.divide(-2, -2), -4)


if __name__ == '__main__':
    unittest.main()

