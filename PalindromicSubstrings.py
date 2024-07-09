class Solution(object):
    def countSubstrings(self, s):
        def is_palindrome(s):
            return s == s[::-1]

        res = 0

        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                if is_palindrome(s[i:j]):
                    res += 1

        return res
    
# Faster solution:

class Solution(object):
    def countSubstrings(self, s):
        def expand_around_center(left, right):
            count = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
            return count

        res = 0
        for i in range(len(s)):
            # Odd length palindromes
            res += expand_around_center(i, i)
            # Even length palindromes
            res += expand_around_center(i, i + 1)

        return res