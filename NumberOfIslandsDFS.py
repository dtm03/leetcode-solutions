class Solution(object):
    def numIslands(self, grid):

        if len(grid) < 1:
            return 0

        islands = 0

        for r in range(0, len(grid)):
            for c in range(0, len(grid[0])):
                if grid[r][c] == '1':
                    self.find(r, c, grid)
                    islands += 1

        return islands

    def find(self, r, c, grid):

        if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
            return

        if grid[r][c] == '1':
            grid[r][c] = '0'
            self.find(r - 1, c, grid)
            self.find(r + 1, c, grid)
            self.find(r, c - 1, grid)
            self.find(r, c + 1, grid)

        