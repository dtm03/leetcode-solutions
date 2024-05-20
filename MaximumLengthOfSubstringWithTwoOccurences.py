from collections import Counter

class Solution(object):
    def maximumLengthSubstring(self, s):
        count = Counter()
        maximum = left = 0

        for right in range(len(s)):
            count[s[right]] += 1

            while count[s[right]] > 2:
                count[s[left]] -= 1
                left += 1

            maximum = max(maximum, right - left + 1)

        return maximum
