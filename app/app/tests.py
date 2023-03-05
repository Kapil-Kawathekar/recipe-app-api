"""
Sample Test
"""


from django.test import SimpleTestCase
from app import calc


class CalcTests(SimpleTestCase):
    """Test Calc module"""

    def test_add_numbers(self):
        """Test adding of two numbers"""
        res = calc.add(5, 6)
        self.assertEqual(res, 11)

    def test_substract_numbers(self):
        """Test substracting of two numbers"""
        res = calc.substract(6, 5)
        self.assertEqual(res, 1)
