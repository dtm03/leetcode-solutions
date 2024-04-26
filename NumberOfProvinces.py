class Solution(object):
    def findCircleNum(self, isConnected):
        def dfs(city):
            visited.add(city)
            for neighbor in range(cols):
                if isConnected[city][neighbor] == 1 and neighbor not in visited:
                    dfs(neighbor)

        provinces = 0
        visited = set()
        rows = len(isConnected)
        cols = len(isConnected[0])

        for city in range(rows):
            if city not in visited:
                dfs(city)
                provinces += 1

        return provinces