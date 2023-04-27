def max_teams(a, b):
    return min(a, b, (a + b) // 4)

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    print(max_teams(a, b))
