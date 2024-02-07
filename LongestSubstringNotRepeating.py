# The goal is to find the longest substring without repeating characters in a given string -> sliding window

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        # Initialize a char set, a pointer and a return value
        charSet = set()
        l = 0
        res = 0

        # Iterate through the string using r as a pointer
        for r in range(len(s)):

        # While the character remains a duplicate
            while s[r] in charSet:

        # Remove the left-most character and update the pointer
                charSet.remove(s[l])
                l += 1

        # Resets the window, so the substring doesn't have dublicates


        # Adds the character (that's now not a duplicate anymore) to the set
            charSet.add(s[r])

        # Potentially updates the substring-length
            res = max(res, r - l + 1)

        return res

