import heapq

n, m = map(int, input().split())

adjacency_list = [[] for _ in range(n)]
for _ in range(m):
    u, v, w = map(int, input().split())
    u -= 1  
    v -= 1  
    adjacency_list[u].append((v, w))
    adjacency_list[v].append((u, w))

# Dijkstra's algorithm
distance = [float('inf')] * n
parent = [-1] * n
distance[0] = 0
heap = [(0, 0)]

while heap:
    dist_u, u = heapq.heappop(heap)
    if dist_u > distance[u]:
        continue
    for v, w in adjacency_list[u]:
        if distance[u] + w < distance[v]:
            distance[v] = distance[u] + w
            parent[v] = u
            heapq.heappush(heap, (distance[v], v))

# Reconstruct the shortest path
if distance[n - 1] == float('inf'):
    print("-1")  # No path exists
else:
    path = []
    v = n - 1
    while v != -1:
        path.append(v + 1)  # Convert back to 1-based indexing
        v = parent[v]
    path.reverse()
    print(" ".join(map(str, path)))
