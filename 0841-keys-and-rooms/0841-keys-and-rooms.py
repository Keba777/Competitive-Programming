class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = [False] * len(rooms)
        visited[0] = True
        
        # Helper function to visit the room
        def visit_room(room):
            for key in rooms[room]:
                if not visited[key]:
                    visited[key] = True
                    visit_room(key)
                    
        visit_room(0)
        return all(visited)
