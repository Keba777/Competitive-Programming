class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for (u, v, w) in times:
            graph[u].append((v, w))

        def dijkstra(graph, start_node):
            time = {node: float('inf') for node in range(1, n + 1)}
            time[start_node] = 0
            visited = set()

            heap = [(0, start_node)]
            while heap:
                cur_time, cur_node = heapq.heappop(heap)

                if cur_node in visited:
                    continue
                visited.add(cur_node)

                for neighbor, edge_time in graph[cur_node]:
                    new_time = time[cur_node] + edge_time
                    if new_time < time[neighbor]:
                        time[neighbor] = new_time
                        heapq.heappush(heap, (new_time, neighbor))

            max_time = max(time.values())
            return max_time if max_time != float('inf') else -1

        return dijkstra(graph, k)
