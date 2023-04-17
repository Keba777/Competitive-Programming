from sys import stdin

def main():
    q = int(input())
    for _ in range(q):
        n = int(input())
        sticks = list(map(int, input().split()))
        sticks.sort()

        area = sticks[0] * sticks[-1]
        valid = True
        i = 0
        j = len(sticks) - 1

        while i < j:
            if sticks[i] != sticks[i + 1] or sticks[j] != sticks[j - 1] or sticks[i] * sticks[j] != area:
                valid = False
                break
            i += 2
            j -= 2

        if valid:
            print("YES")
        else:
            print("NO")

if __name__ == '__main__':
    main()
