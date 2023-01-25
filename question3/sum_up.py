# The function sum_up receives an integer and returns the sum of its digits
def sum_up(num: int) -> int:
    if num//10 == 0:
        return num % 10
    return sum_up(num//10) + num % 10

# Testing the function with the example given in the task
# There are 2 additional tests in test_price_check.py
def main():
    print(sum_up(2347623))

if __name__ == '__main__':
    main()
