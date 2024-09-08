class Solution(object):
    def robotSim(self, commands, obstacles):
        # Directions: North, East, South, West
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        currPos = (0, 0)
        currDir = 0
        maxDist = 0
        obstacle_set = set(map(tuple, obstacles))  # Convert obstacles list to a set of tuples for fast lookup

        for c in commands:
            if c == -2:
                # Turn left 90 degrees
                currDir = (currDir - 1) % 4
            elif c == -1:
                # Turn right 90 degrees
                currDir = (currDir + 1) % 4
            else:
                for _ in range(c):
                    # Calculate the next position
                    nextPos = (currPos[0] + directions[currDir][0], currPos[1] + directions[currDir][1])
                    # Check if the next position is an obstacle
                    if nextPos in obstacle_set:
                        break
                    # Move to the next position
                    currPos = nextPos
                    # Calculate the squared distance from the origin
                    maxDist = max(maxDist, currPos[0]**2 + currPos[1]**2)

        return maxDist
