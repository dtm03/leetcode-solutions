# Sure, let me explain the code step by step:
#
# The nearestExit function takes two arguments: maze, which is a 2D list representing the maze, and entrance, which is a tuple (row, column) indicating the starting point in the maze.
# It initializes some variables:
# r and c represent the number of rows and columns in the maze respectively.
# sx and sy represent the starting coordinates (entrance) in the maze.
# q is a deque used for breadth-first search.
#     distance is a 2D list used to keep track of the minimum distance from the entrance to each cell in the maze. It is initialized with a large value initially.
# The enqueue function is defined to add a cell (x, y) with distance d to the queue and update the distance matrix.
# The starting cell (sx, sy) is enqueued with distance 0.
# directions is a list containing the possible movements: up, down, left, and right.
# The breadth-first search loop starts. While the queue is not empty:
# A cell (x, y) is dequeued from the queue along with its distance d.
# If the dequeued cell is on the boundary of the maze and is not the starting cell, its distance is returned. This is because we are looking for the nearest exit, and once we reach a boundary cell, we have found an exit.
# Otherwise, for each direction, if the adjacent cell (nx, ny) is within the maze boundaries, not blocked by a wall ("+"), and hasn't been visited yet (checked by comparing its distance with a large value), it is enqueued with distance d + 1. If the adjacent cell is on the boundary, its distance is returned since it represents an exit.
# The loop continues until all possible paths are explored.
# If no exit is found, -1 is returned, indicating that there is no exit reachable from the entrance.
# This algorithm performs a breadth-first search from the entrance of the maze, exploring all possible paths until it finds the nearest exit. If no exit is found, it returns -1.

import collections


class Solution(object):
    def nearestExit(self, maze, entrance):
        r, c = len(maze), len(maze[0])
        sx, sy = entrance
        q = collections.deque()
        distance = [[10 ** 20] * c for _ in range(r)]

        def enqueue(x, y, d):
            distance[x][y] = d
            q.append((x, y, d))

        enqueue(sx, sy, 0)

        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        while len(q) > 0:
            x, y, d = q.popleft()

            if x == 0 or x == r - 1 or y == 0 or y == c - 1:
                if not (x == sx and y == sy):
                    return d

            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if 0 <= nx < r and 0 <= ny < c and maze[nx][ny] !="+" and distance[nx][ny] == 10 ** 20:
                    enqueue(nx, ny, d + 1)
                    if nx == 0 or nx == r - 1 or ny == 0 or ny == c - 1:
                        return d + 1

        return -1