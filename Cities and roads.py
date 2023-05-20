def main():
    n = int(input().strip())
    matrix = [list(map(int, input().strip().split())) for _ in range(n)]
    roads = 0

    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 1:
                roads += 1

    print(roads // 2)

main()
