class Solution(object):
    def getMinSwaps(self, num, k):
        # Helper function to find the next lexicographical permutation
        def next_permutation(s):
            s = list(s)
            i = len(s) - 2
            while i >= 0 and s[i] >= s[i + 1]:
                i -= 1
            if i == -1:
                return ''.join(s[::-1])
            j = len(s) - 1
            while s[j] <= s[i]:
                j -= 1
            s[i], s[j] = s[j], s[i]
            return ''.join(s[:i+1] + s[i+1:][::-1])

        # Generate the k-th permutation
        target = num
        for _ in range(k):
            target = next_permutation(target)

        # Count the minimum swaps to convert num to target
        num = list(num)
        target = list(target)
        swaps = 0
        for i in range(len(num)):
            if num[i] != target[i]:
                j = i
                while num[j] != target[i]:
                    j += 1
                while j > i:
                    num[j], num[j-1] = num[j-1], num[j]
                    j -= 1
                    swaps += 1
        return swaps