class Solution(object):
    def missingRolls(self, rolls, mean, n):
        # Total number of dice (already rolled + missing rolls)
        total = len(rolls) + n

        # The total sum needed to achieve the desired mean
        required_sum = total * mean

        # The sum of the already known rolls
        current_sum = sum(rolls)

        # The remaining sum that needs to be distributed among the missing rolls
        missing_sum = required_sum - current_sum

        # Check if it's possible to divide the remaining sum among the missing rolls
        if missing_sum < n or missing_sum > 6 * n:
            return []  # Impossible to find a valid solution

        # We start by giving each missing roll a value of 1
        res = [1] * n
        remaining = missing_sum - n  # We've already given 1 to each roll

        # Distribute the remaining sum across the dice, without exceeding 6 per dice
        i = 0
        while remaining > 0:
            add = min(5, remaining)  # We can add at most 5 to any dice (1 + 5 = 6)
            res[i] += add
            remaining -= add
            i += 1

        return res