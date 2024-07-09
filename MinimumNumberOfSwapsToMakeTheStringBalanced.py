class Solution(object):
    def minSwaps(self, s):
        balance = 0
        max_imbalance = 0

        # Traverse the string to find the maximum imbalance
        for char in s:
            if char == '[':
                balance += 1
            else:
                balance -= 1
            # Track the most negative balance encountered
            max_imbalance = min(max_imbalance, balance)

        # The minimum number of swaps needed is half the maximum imbalance (negative value)
        return (-max_imbalance + 1) // 2
        