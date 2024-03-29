"""sample tests"""
from django.test import SimpleTestCase
from app import calc


class CalcTests(SimpleTestCase):
    """test the calc module"""

    def test_add_numbers(self):
        """adding together"""
        res = calc.add(5, 6)
        self.assertEqual(res, 11)

    def test_subtract_numbers(self):
        """adding together"""
        res = calc.subtract(5, 6)
        self.assertEqual(res, -1)
