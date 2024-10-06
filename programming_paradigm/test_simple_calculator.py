import unittest

from simple_calculator import SimpleCalculator

class TestClass(unittest.TestCase):
    def CallSc(self):
        self.calc=SimpleCalculator()
    
    def test_addition(self):
        self.assertEqual(self.calc.add(5,8),13)
    
    def test_divide(self):
        self.assertEqual(self.calc.divide(4,2),2)

    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(5,2),3)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(3,5), 15)