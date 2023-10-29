import heapq

mx = 401

rail = [[] for _ in range(mx)]
bus = [[] for _ in range(mx)]
s = set()
dist_rail = [float('inf')] * mx
dist_bus = [float('inf')] * mx
vis = [False] * mx

def dijkstra(adj, dist):
    pq = [(0, 1)]
    dist[1] = 0
    while pq:
        d, u = heapq.heappop(pq)
        if vis[u]:
            continue
        vis[u] = True
        for v, weight in adj[u]:
            if dist[v] > dist[u] + weight:
                dist[v] = dist[u] + weight
                heapq.heappush(pq, (dist[v], v))

n, m = map(int, input().split())
for _ in range(m):
    a, b = map(int, input().split())
    rail[a].append((b, 1))
    rail[b].append((a, 1))
    s.add((min(a, b), max(a, b)))

for i in range(1, n + 1):
    dist_rail[i] = float('inf')
    dist_bus[i] = float('inf')
    vis[i] = False

dijkstra(rail, dist_rail)

for i in range(1, n + 1):
    vis[i] = False

for i in range(1, n + 1):
    for j in range(i + 1, n + 1):
        p = (i, j)
        if p not in s:
            bus[i].append((j, 1))
            bus[j].append((i, 1))

dijkstra(bus, dist_bus)

if dist_bus[n] == float('inf') or dist_rail[n] == float('inf'):
    print("-1")
else:
    print(max(dist_bus[n], dist_rail[n]))
