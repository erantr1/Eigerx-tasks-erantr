from typing import List


def max_num_update(max_result: List[int]) -> List[int]:
    try:
        num = int(input("Enter the next number\n"))
    except ValueError:
        print("Inputs must be integers")
        exit(0)
    if num == 0:
        return max_result
    if num > max_result[0]:
        max_result[0] = num
        max_result[1] = 1
    elif num == max_result[0]:
        max_result[1] += 1
    max_num_update(max_result)
    return max_result


def main():
    try:
        num = int(input("Enter the first number\n"))
    except ValueError:
        print("Inputs must be integers")
        exit(0)
    max_result = [num, 1]
    if int(num) == 0:
        print("The sequence must include at least one non-zero element")
    else:
        max_num_update(max_result)
        print(f"({';'.join(str(elem) for elem in max_result)})")
        # The print above is rather ugly, but so is this alternative: print(f"({max_result[0]}; {max_result[1]})")


if __name__ == '__main__':
    main()
