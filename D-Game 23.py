n, m = map(int, input().split())


def main(n, m):
    if n == m:
        return 0
    if n > m:
        return -1

    count2 = main(n * 2, m)
    count3 = main(n * 3, m)

    if count2 == -1 and count3 == -1:
        return -1
    elif count2 == -1:
        return count3 + 1
    elif count3 == -1:
        return count2 + 1
    else:
        return min(count2, count3) + 1


print(main(n, m))
