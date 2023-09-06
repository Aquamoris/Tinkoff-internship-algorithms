def third_task():
    n = int(input())

    first = list(map(int, input().split()))
    second = list(map(int, input().split()))

    start = 0
    finish = 0

    for i in range(n):
        if first[i] != second[i]:
            start = i
            break

    for j in range(start + 1, n):
        if first[j] == second[j]:
            finish = j
            break

    sorting_part = first[start:finish]

    sorting_part.sort()

    first[start:finish] = sorting_part

    print('YES') if first == second else print('NO')


if __name__ == '__main__':
    third_task()