def sum_up(num):
    if num//10 == 0:
        return num % 10
    return sum_up(num//10) + num % 10


def main():
    print(sum_up(2347623))


if __name__ == '__main__':
    main()
