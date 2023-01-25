from typing import List


def verify_constraints(products: List[str], product_prices: List[float], product_sold: List[str], sold_price: List[float]) -> bool:
    assert (0 < len(products) < 100), "The number of products must be between 1 and 99"
    assert (0 < len(product_prices) <= 100),\
        "The number of products prices must be between 1 and 99"
    assert (len(product_prices) == len (products)),\
        "The number of products prices must be equal to the number of products"
    assert (0 < len(product_sold) <= 100), "The number of sold products must be between 1 and 99"
    assert (0 < len(sold_price) <= 100), "The number of sold products prices must be between 1 and 99"
    assert (len(product_sold) == len(sold_price)),\
        "The number of sold products must be equal to the number of sold products prices"
    assert all(item in products for item in product_sold), "All sold products must be part of the products list"
    assert (min(product_prices) >=1 and max(product_prices) <= 100000 and min(sold_price) >= 1 and max(sold_price) <= 100000),\
        "The prices of all products must be between 1 and 100,000"
    return True


# The function price_check receives 2 pairs of lists: catalog products and their prices vs. sold products and the
# prices in which they were sold. The function then compares the prices of the sold products to the ones in the catalog
# and returns the number of errors (mismatches)
def price_check(products: List[str], product_prices: List[float], product_sold: List[str], sold_price: List[float]) ->\
        int:
    # I wasn't sure whether the constraints are to be checked or they can be assumed, so I added a function for
    # verifying them, just in case
    if verify_constraints(products, product_prices, product_sold, sold_price):
        # Converting the lists into dictionaries for better efficiency in the search process hereinafter
        products_dict = dict(zip(products, product_prices))
        sold_dict = dict(zip(product_sold, sold_price))
        errors = 0
        for product in sold_dict:
            if products_dict[product] != sold_dict[product]:
                errors += 1
        return errors


# Testing the function with the example given in the task
# There is one additional test (the 2nd example from the task) in test_price_check.py
def main():
    products = ['eggs', 'milk', 'cheese']
    product_prices = [2.89, 3.29, 5.79]
    product_sold = ['eggs', 'eggs', 'cheese', 'milk']
    sold_price = [2.89, 2.99, 5.97, 3.29]
    num_errors = price_check(products, product_prices, product_sold, sold_price)
    if num_errors is not None:
        print(f"The number of errors is {num_errors}")


if __name__ == '__main__':
    main()
