# Check whether to given strings are anagrams of each other -> Use the build-in python functions

class Solution:
    def isAnagram(selfself, s: str, t: str) -> bool:

        # return sorted(s) == sorted(t)
        # return Counter(s) == Counter(t)

    # Check whether both strings have the same length
        if len(s) != len(t):
            return False

    # Initialize 2 hash-maps
        countS, countT = {}, {}

    # Count the occurences of each letter and save them in the hash-map
        for i in range(len(s)):
            countS[s[i]] = countS.get(s[i], 0) + 1
            countT[t[i]] = countT.get(t[i], 0) + 1

    # Compare the occurences
        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False

        return True