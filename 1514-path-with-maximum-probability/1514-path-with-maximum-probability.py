class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        graph = defaultdict(list)
        for i, (u, v) in enumerate(edges):
            graph[u].append((v, succProb[i]))
            graph[v].append((u, succProb[i]))

        def dijkstra(graph, start_node):
            distances = {node: 0.0 for node in range(n)}
            distances[start_node] = 1.0
            visited = set()

            heap = [(-1.0, start_node)]
            while heap:
                current_prob, current_node = heapq.heappop(heap)
                current_prob = -current_prob  

                if current_node in visited:
                    continue
                visited.add(current_node)

                for neighbor, edge_prob in graph[current_node]:
                    new_prob = distances[current_node] * edge_prob
                    if new_prob > distances[neighbor]:
                        distances[neighbor] = new_prob
                        heapq.heappush(heap, (-new_prob, neighbor))

            return distances[end]

        return dijkstra(graph, start)
