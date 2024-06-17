class Solution(object):
    def longestPalindrome(self, s):
        def expand_around_center(s, left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1 : right]

        res = ""
        for i in range(len(s)):
            # Check for odd-length palindromes
            odd_palindrome = expand_around_center(s, i, i)
            if len(odd_palindrome) > len(res):
                res = odd_palindrome

            # Check for even-length palindromes
            even_palindrome = expand_around_center(s, i, i + 1)
            if len(even_palindrome) > len(res):
                res = even_palindrome

        return res