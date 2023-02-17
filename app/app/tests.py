
from django.test import SimpleTestCase
from app import calc

class CalcTest(SimpleTestCase):
    def test_add_numbers(self):
        res = calc.add(3,5)

        self.assertEqual(res,8)

    def test_sub_numbers(self):
        res=calc.sub(10,20)

        self.assertEqual(res,10)