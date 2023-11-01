def main():
    ttt = int(input())
    for _ in range(ttt):
        n, m = map(int, input().split())
        tmp = input().strip()
        s = int(tmp, 2)
        edges = []
        for i in range(m):
            w = int(input())
            tmp = input().strip()
            x = ((1 << n) - 1) ^ int(tmp, 2)
            tmp = input().strip()
            y = int(tmp, 2)
            edges.append(((x, y), w))
        
        dist = [float('inf')] * (1 << n)
        dist[s] = 0
        q = {(0, s)}
        
        while q:
            d, v = min(q)
            q.remove((d, v))
            for i in range(m):
                to = v & edges[i][0][0]
                to |= edges[i][0][1]
                if dist[to] > d + edges[i][1]:
                    q.discard((dist[to], to))
                    dist[to] = d + edges[i][1]
                    q.add((dist[to], to))
        
        if dist[0] == float('inf'):
            dist[0] = -1
        print(dist[0])

if __name__ == "__main__":
    main()
