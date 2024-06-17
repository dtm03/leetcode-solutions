class Solution(object):
    def shortestToChar(self, s, c):
        n = len(s)
        res = [float('inf')] * n

        # Forward pass: calculate distances from left to right
        cp = float('-inf')
        for i in range(n):
            if s[i] == c:
                cp = i
            res[i] = min(res[i], abs(i - cp))

        # Backward pass: calculate distances from right to left
        cp = float('inf')
        for i in range(n - 1, -1, -1):
            if s[i] == c:
                cp = i
            res[i] = min(res[i], abs(i - cp))

        return res