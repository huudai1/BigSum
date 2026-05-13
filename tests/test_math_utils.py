import unittest
from src.math_utils import MyBigNumber

class TestBigSum(unittest.TestCase):
    def setUp(self):
        self.calc = MyBigNumber()

    def test_basic_addition(self):
        self.assertEqual(self.calc.sum("1234", "897"), "2131")
    
    def test_different_lengths(self):
        self.assertEqual(self.calc.sum("1", "999"), "1000")
        self.assertEqual(self.calc.sum("999", "1"), "1000")
    
    def test_equal_lengths(self):
        self.assertEqual(self.calc.sum("123", "456"), "579")
    
    def test_carry_over_at_end(self):
        self.assertEqual(self.calc.sum("99", "1"), "100")
        self.assertEqual(self.calc.sum("50", "50"), "100")
        
    def test_large_numbers(self):
        num1 = "1" * 100
        num2 = "1" * 100
        expected = "2" * 100
        self.assertEqual(self.calc.sum(num1, num2), expected)

if __name__ == "__main__":
    unittest.main()

