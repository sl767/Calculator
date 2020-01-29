import unittest

from Calculator.Calculator import Calculator

class MyTestCase(unittest.TestCase):

    def test_instantiate_calculator(self):
        calculator = Calculator()
        self.assertIsInstance(calculator, Calculator)
    def test_calculator_addition(self):
        calculator = Calculator()
        result = calculator.addition(1,2)
        self.assertEqual(3, result)
    def test_calculator_subrtraction(self):
        calculator = Calculator()
        result = calculator.subtraction(1,2)
        self.assertEqual(-1, result)
    def test_calculator_multiplication(self):
        calculator = Calculator()
        result = calculator.multiplication(1,2)
        self.assertEqual(2, result)
    def test_calculator_division(self):
        calculator = Calculator()
        result = calculator.division(4,2)
        self.assertEqual(2, result)
    def test_calculator_square(self):
        calculator = Calculator()
        result = calculator.square(6)
        self.assertEqual(36, result)
    def test_calculator_squareroot(self):
        calculator = Calculator()
        result = calculator.squareroot(25)
        self.assertEqual(5, result)


if __name__ == '__main__':
    unittest.main()