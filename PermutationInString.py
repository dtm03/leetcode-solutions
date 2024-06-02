class Solution(object):
    def checkInclusion(self, s1, s2):
        if len(s1) > len(s2):
            return False

        s1_count = {}
        for char in s1:
            s1_count[char] = s1_count.get(char, 0) + 1

        window_count = {}
        for i in range(len(s1)):
            window_count[s2[i]] = window_count.get(s2[i], 0) + 1

        if window_count == s1_count:
            return True

        for i in range(len(s1), len(s2)):
            if window_count[s2[i - len(s1)]] == 1:
                del window_count[s2[i - len(s1)]]
            else:
                window_count[s2[i - len(s1)]] -= 1

            window_count[s2[i]] = window_count.get(s2[i], 0) + 1

            if window_count == s1_count:
                return True

        return False


# Shorter but way slower solution:
# class Solution(object):
#     def checkInclusion(self, s1, s2):
#         N = r = len(s1)
#
#         while r <= len(s2):
#             sub = s2[r - N : r]
#             if sorted(sub) == sorted(s1):
#                 return True