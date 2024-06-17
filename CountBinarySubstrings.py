class Solution(object):
    def countBinarySubstrings(self, s):
        res = 0
        prev_count = 0
        cur_count = 1

        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                cur_count += 1
            else:
                res += min(prev_count, cur_count)
                prev_count = cur_count
                cur_count = 1

        res += min(prev_count, cur_count)

        return res