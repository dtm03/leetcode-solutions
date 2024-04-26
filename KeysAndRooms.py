# Use DFS

class Solution(object):
    def canVisitAllRooms(self, rooms):
        visited = set()
        to_visit = {0}
        while to_visit:
            cur = to_visit.pop()
            visited.add(cur)
            for next in rooms[cur]:
                if next not in visited:
                    to_visit.add(next)
        return len(visited) == len(rooms)