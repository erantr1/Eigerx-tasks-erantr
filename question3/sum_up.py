def sum_up(num):
    sum_of_digits = 0
    if num//10 > 0:
        sum_of_digits += sum_up(num//10) + num % 10
    else:
        sum_of_digits += num % 10
    return sum_of_digits


def main():
    print(sum_up(2347623))


if __name__ == '__main__':
    main()
