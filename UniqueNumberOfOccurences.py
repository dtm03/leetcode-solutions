# Check whether each value in a given array is unique -> Count occurences in a hash-map

from collections import Counter

class Solution(object):
    def uniqueOccurrences(self, arr):

    # Count the occurences of each value in the array
        occ = Counter(arr).values()

    # Check whether the length of the array is equal to the length of the set of occurences
        return len(occ) == len(set(occ))