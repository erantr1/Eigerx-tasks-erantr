from unittest import TestCase
from sum_up import sum_up


class TestSum(TestCase):
    def test_sum_up(self):
        self.assertEqual(sum_up(323462), 20)
        self.assertEqual((sum_up(987654321)), sum_up(123456789))
