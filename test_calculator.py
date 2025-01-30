import unittest
from calculator import StringCalculator

class TestStringCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = StringCalculator()

    def test_empty_string(self):
        self.assertEqual(self.calculator.add(""), 0)

    def test_single_number(self):
        self.assertEqual(self.calculator.add("5"), 5)

    def test_two_numbers(self):
        self.assertEqual(self.calculator.add("1,2"), 3)

    def test_newline_delimiter(self):
        self.assertEqual(self.calculator.add("1\n2,3"), 6)

    def test_custom_delimiter(self):
        self.assertEqual(self.calculator.add("//;\n1;2"), 3)

    def test_negative_number(self):
        with self.assertRaises(ValueError) as context:
            self.calculator.add("1,-2,3")
        self.assertIn("Negatives not allowed: [-2]", str(context.exception))
