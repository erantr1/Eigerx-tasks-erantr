from typing import List


def verify_constraints(products: List[str], product_prices: List[float], product_sold: List[str], sold_price: List[float]) -> bool:
    if len(products) < 1 or len(products) > 100:
        print("The number of products must be between 1 and 99")
        return False
    elif len(product_prices) < 1 or len(product_prices) > 100:
        print("The number of products prices must be between 1 and 99")
        return False
    elif len(product_prices) != len (products):
        print("The number of products prices must be equal to the number of products")
        return False
    elif len(product_sold) < 1 or len(product_sold) > 100:
        print("The number of sold products must be between 1 and 99")
        return False
    elif len(sold_price) < 1 or len(sold_price) > 100:
        print("The number of sold products prices must be between 1 and 99")
        return False
    elif len(product_sold) != len(sold_price):
        print("The number of sold products must be equal to the number of sold products prices")
        return False
    elif not all(item in products for item in product_sold):
        print("All sold products must be part of the products list")
        return False
    elif len(product_prices) < 1 or len(product_prices) > 100000 or len(sold_price) < 1 or len(sold_price) > 100000:
        print("The prices of all products must be between 1 and 100,000")
        return False
    else:
        return True


def price_check(products: List[str], product_prices: List[float], product_sold: List[str], sold_price: List[float]) -> int:
    if verify_constraints(products, product_prices, product_sold, sold_price):
        errors = 0
        for i in range(len(sold_price)):
            product = product_sold[i]
            product_index = products.index(product)
            if product_prices[product_index] != sold_price[i]:
                errors += 1
        return errors


def main():
    products = ['rice', 'sugar', 'wheat', 'cheese']
    product_prices = [16.89, 56.92, 20.89, 345.99]
    product_sold = ['rice', 'cheese']
    sold_price = [18.99, 400.89]
    num_of_errors = price_check(products, product_prices, product_sold, sold_price)
    print(f"The number of errors is {num_of_errors}") ## Only if num_of_erros is not None


if __name__ == '__main__':
    main()
