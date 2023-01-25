from unittest import TestCase
from price_check import price_check


class TestPrices(TestCase):
    def test_price_check(self):
        products = ['rice', 'sugar', 'wheat', 'cheese']
        product_prices = [16.89, 56.92, 20.89, 345.99]
        product_sold = ['rice', 'cheese']
        sold_price = [18.99, 400.89]
        self.assertEqual(price_check(products, product_prices, product_sold, sold_price), 2)
