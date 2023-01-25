# The function max_num_update receives a stream of integers from a user and returns the number with most records,
# together with the number of that record
def max_num_update(max_value: int, max_counter: int) -> [int, int]:
    try:
        num = int(input("Enter the next number\n"))
    except ValueError:
        print("Error: the inputs must be an integer")
        exit(0)
    if num == 0:
        return max_value, max_counter
    if num > max_value:
        max_value = num
        max_counter = 1
    elif num == max_value:
        max_counter += 1
    return max_num_update(max_value, max_counter)


def main():
    try:
        num = int(input("Enter the first number\n"))
    except ValueError:
        print("Error: the inputs must be an integer")
        exit(0)
    if num == 0:
        print("The sequence must include at least one non-zero element")
    else:
        max_value, max_counter = max_num_update(num, 1)
        print(f"({max_value}; {max_counter})")


if __name__ == '__main__':
    main()
