class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(list)
        for prerequisite in prerequisites:
            a, b = prerequisite
            graph[a].append(b)

        def dijkstra(start):
            shortest_paths = [-1] * numCourses
            shortest_paths[start] = 0
            heap = [(0, start)]

            while heap:
                path_length, course = heapq.heappop(heap)
                if shortest_paths[course] < path_length:
                    continue
                for next_course in graph[course]:
                    new_length = path_length + 1
                    if shortest_paths[next_course] == -1 or new_length < shortest_paths[next_course]:
                        shortest_paths[next_course] = new_length
                        heapq.heappush(heap, (new_length, next_course))
            return shortest_paths

        answer = []
        for uj, vj in queries:
            shortest_paths = dijkstra(uj)
            if shortest_paths[vj] != -1:
                answer.append(True)
            else:
                answer.append(False)

        return answer