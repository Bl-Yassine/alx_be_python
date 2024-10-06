import unittest

from simple_calculator import SimpleCalculator

class TestClass(unittest.TestCase):
    def CallSc(self):
        self.calc=SimpleCalculator()
    
    def testAdd(self):
        self.assertEqual(self.calc.add(5,8),13)
    
    def testDiv(self):
        self.assertEqual(self.calc.divide(4,2),2)
