def main():
    n, d = read_long_pair()
    N = read_long_array()

    N.sort()

    wins = 0
    players = 0

    for i in range(n - 1, players - 1, -1):
        if N[i] > d:
            wins += 1
            continue

        team = d // N[i]
        players += team
        if players <= i:
            wins += 1

    print(wins)

def read_int():
    return int(input())

def read_long():
    return int(input())

def read_int_pair():
    s = input().split()
    return int(s[0]), int(s[1])

def read_long_pair():
    s = input().split()
    return int(s[0]), int(s[1])

def read_int_array():
    return list(map(int, input().split()))

def read_long_array():
    return list(map(int, input().split()))

def read_string_array():
    return input().split()

if __name__ == "__main__":
    main()
