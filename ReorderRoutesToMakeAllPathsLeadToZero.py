from collections import defaultdict

class Solution(object):
    def minReorder(self, n, connections):
        adj = defaultdict(list)
        for src, dest in connections:
            adj[src].append((dest, 1))
            adj[dest].append((src, 0))

        visit = set()

        def dfs(n = 0, cnt = 0):
            visit.add(n)
            for nei, wei in adj[n]:
                if nei in visit: continue
                cnt = dfs(nei, cnt + wei)
            return cnt

        return dfs()