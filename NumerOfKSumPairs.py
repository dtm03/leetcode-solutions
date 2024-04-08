from collections import Counter

# The goal is to return the number of pairs in an array nums that add up to a given number k


class Solution(object):
    def maxOperations(self, nums, k):
        freq = Counter(nums)

        pairs = 0
        for key in freq.keys():
            a, b = key, k - key

            # This condition avoids pairs being counted twice
            if a < b:

                # This checks whether the needed difference from the key is in the array
                # Than it calculates the minimum frequency, meaning how many pairs can be built
                pairs += min(freq[a], freq[b])

            # If the key is exactly have of the given number k you can just add the frequence divided by two since
            # 2 of the numbers make up k
            elif a == b:
                pairs += freq[a] // 2
        return pairs