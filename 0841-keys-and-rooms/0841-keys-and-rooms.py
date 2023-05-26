class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        # BFS
        visited = set()
        queue = deque([0])

        while queue:
            cur_room = queue.popleft()
            visited.add(cur_room)

            for key in rooms[cur_room]:
                if key not in visited:
                    queue.append(key)

        return len(visited) == len(rooms)


        # DFS
        # visited = [False] * len(rooms)
        # visited[0] = True
        
        # # Helper function to visit the room
        # def visit_room(room):
        #     for key in rooms[room]:
        #         if not visited[key]:
        #             visited[key] = True
        #             visit_room(key)
                    
        # visit_room(0)
        # return all(visited)
