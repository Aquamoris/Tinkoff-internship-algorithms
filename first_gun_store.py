def first_task():
    first = input().split()
    second = input().split()

    first = list(map(int, first))
    second = list(map(int, second))

    result = 0

    for price in second:
        if first[1] >= price > result:
            result = price

    print(result)


if __name__ == '__main__':
    first_task()
