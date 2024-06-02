class Solution(object):
    def findAnagrams(self, s, p):
        res = []
        lp = len(p)
        sorted_p = sorted(p)
        for i in range(lp, len(s) + 1):  # Adjust the range to include the last substring
            if sorted(s[i - lp:i]) == sorted_p:  # Sort both substrings and compare
                res.append(i - lp)
        return res

from collections import Counter

# class Solution(object):
#     def findAnagrams(self, s, p):
#         res = []
#         if len(s) < len(p):
#             return res
#
#         p_count = Counter(p)
#         s_count = Counter(s[:len(p)])
#
#         if p_count == s_count:
#             res.append(0)
#
#         for i in range(len(p), len(s)):
#             # Add the new character to the window
#             s_count[s[i]] += 1
#
#             # Remove the leftmost character from the window
#             s_count[s[i - len(p)]] -= 1
#             if s_count[s[i - len(p)]] == 0:
#                 del s_count[s[i - len(p)]]
#
#             # Check if the counts match
#             if p_count == s_count:
#                 res.append(i - len(p) + 1)
#
#         return res
