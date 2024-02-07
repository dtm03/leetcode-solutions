# The goal is to check whether a string is a palindrome.

class Solution(object):
    def isPalindrome(self, s: str):

        # Clean the string using text comprehension.
        s = ''.join(char for char in s if char.isalnum()).lower()

        return s == s[::-1]