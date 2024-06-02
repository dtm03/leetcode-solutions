from collections import Counter
from string import ascii_uppercase

class Solution(object):
    def uniqueLetterString(self, S):
        index = {c: [-1, -1] for c in ascii_uppercase}
        res = 0
        for i, c in enumerate(S):
            k, j = index[c]
            res += (i - j) * (j - k)
            index[c] = [j, i]
        for c in index:
            k, j = index[c]
            res += (len(S) - j) * (j - k)
        return res % (10**9 + 7)

# Longer solution
from collections import Counter
# class Solution(object):
#     def uniqueLetterString(self, s):
#
#         def countUniqueChars(sub):
#             cc = Counter(sub)
#             u = 0
#             for c in cc.values():
#                 if c == 1:
#                     u += 1
#             return u
#
#         res = 0
#         n = len(s)
#
#         # Loop through all possible starting points of substrings
#         for i in range(n):
#             cc = Counter()
#             unique_count = 0
#
#             # Expand the window from the starting point to find substrings
#             for j in range(i, n):
#                 cc[s[j]] += 1
#                 if cc[s[j]] == 1:
#                     unique_count += 1
#                 elif cc[s[j]] == 2:
#                     unique_count -= 1
#                 res += unique_count
#
#         return res