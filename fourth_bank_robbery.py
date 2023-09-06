def fourth_task():
    first = list(map(int, input().split()))
    second = list(map(int, input().split()))

    n, m = first[0], first[1]

    second *= 2
    second.sort()
    second.reverse()

    i = 0

    coins = []

    for coin in second:
        n -= coin
        if n == 0:
            i += 1
            coins.append(coin)
            break
        elif n < 0:
            n += coin
        else:
            i += 1
            coins.append(coin)

    coins.reverse()

    if n == 0:
        print(i)
        for i in coins:
            print(i)
    else:
        print(-1)


if __name__ == '__main__':
    fourth_task()