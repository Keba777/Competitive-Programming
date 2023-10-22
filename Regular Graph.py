from collections import defaultdict

# Read input
n, m = map(int, input().split())
graph = defaultdict(list)

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

degree = len(graph[1])

is_regular = all(len(neighbour) == degree for neighbour in graph.values())

if is_regular:
    print("YES")
else:
    print("NO")
