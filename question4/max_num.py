def max_num_update(num, max_result):
    num = int(input("Enter the next number\n"))
    if num == 0:
        return max_result
    if num > max_result[0]:
        max_result[0] = num
        max_result[1] = 1
    elif num == max_result[0]:
        max_result[1] += 1
    max_num_update(num, max_result)
    return max_result


def main():
    num = int(input("Enter the first number\n"))
    max_result = [num, 1]
    if int(num) == 0:
        print("The sequence must include at least one non-zero element")
    else:
        max_num_update(num, max_result)
        print(max_result)


if __name__ == '__main__':
    main()


## annotations
## empty input protection