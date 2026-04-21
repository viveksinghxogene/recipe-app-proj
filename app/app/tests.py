""" 
Sample tests
"""
from django.test import SimpleTestCase
from app import calc 
class CalcTest(SimpleTestCase):
    """Test the calc module eagerly"""
    def test_add_numbers(self):
        """Test adding the numbers together"""
        res = calc.add(5,6)
        self.assertEqual(res,11)
        #first i have written this and eventually it fails 
        #due to TTD pracctice that I am doing
    def test_sub_number(self):
        res=calc.subtract(10,4)
        self.assertEqual(res,6)
    def test_sub_number_fails(self):
        #i tried to explicitly make this wrong as well.
        res = calc.subtract(80, 10)
        self.assertNotEqual(90, res)