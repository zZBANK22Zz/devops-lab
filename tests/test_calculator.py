import unittest
from app.calculator import add, subtract, divide, multiply

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2,3),5)
    
    def test_subtract(self):
        self.assertEqual(subtract(10,4),6)

    def test_multiply(self):
        self.assertEqual(multiply(3,7),21)

    def test_divide(self):
        self.assertEqual(divide(10,2),5)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide(10, 0)

if __name__ == '__main__':
    unittest.main();