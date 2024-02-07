# The goal is to find the minimum cost to reach the top of the floor, and you can either start from the step with index 0,
# or the step with index 1. => Iterate and update

class Solution(object):
    def minCostClimbingStairs(self, cost):

        prev1, prev2 = cost[0], cost[1]

        # Iterate from the third step to the top
        for i in range(2, len(cost)):

            # Calculate the minimum cost to reach the current step
            current_cost = cost[i] + min(prev1, prev2)

            # Update the variables for the last two steps
            prev1, prev2 = prev2, current_cost

        # The minimum cost to reach the top is the minimum of the last two steps
        return min(prev1, prev2)