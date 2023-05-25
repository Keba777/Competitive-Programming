def main():
    n = int(input().strip())
    adj_list = []
    for _ in range(n):
        adj_list.append(list(map(int, input().split()))[1:])
    adj_matrix = [[0]*n for _ in range(n)]
    for i, row in enumerate(adj_list):
        for j in row:
            adj_matrix[i][j-1] = 1
    for row in adj_matrix:
        print(" ".join(str(x) for x in row))

main()
