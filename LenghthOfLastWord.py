# The goal is to find the length of the last word => Use regex

import re

class Solution(object):
    def lengthOfLastWord(self, s):
        return len(re.findall(r'\w+', s)[-1])

'''
re.findall(): This function is used to search for all occurrences of a regular expression pattern in a given string 
and return them as a list.

r'\w+': This is the regular expression pattern. It consists of the following components:

\w: This is a shorthand character class that matches any word character. It includes letters (both uppercase and lowercase), 
digits, and underscores.
+: This quantifier means "one or more." It specifies that we want to match one or more consecutive word characters.
So, when you use re.findall(r'\w+', s), it finds all the sequences of word characters in the input string s, 
effectively splitting the string into words. 
This is a common technique for tokenizing a string into words, ignoring spaces, punctuation, and other non-word characters.
'''