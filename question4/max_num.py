def max_num_update(max_result: int, max_counter: int) -> [int, int]:
    try:
        num = int(input("Enter the next number\n"))
    except ValueError:
        print("Inputs must be integers")
        exit(0)
    if num == 0:
        return max_result, max_counter
    if num > max_result:
        max_result = num
        max_counter = 1
    elif num == max_result:
        max_counter += 1
    max_result, max_counter = max_num_update(max_result, max_counter)
    return max_result, max_counter


def main():
    try:
        num = int(input("Enter the first number\n"))
    except ValueError:
        print("Inputs must be integers")
        exit(0)
    # max_result = [num, 1]
    if int(num) == 0:
        print("The sequence must include at least one non-zero element")
    else:
        max_result = num
        max_counter = 1
        max_result, max_counter = max_num_update(max_result, max_counter)
        print(f"({max_result}; {max_counter})")


if __name__ == '__main__':
    main()
