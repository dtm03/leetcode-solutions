# Check whether the parentheses in a given string are valid -> Push open brackets in a stack and pop them if they are closed

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

    # Initializes an empty stack and a hash-map containing all possible combinations
        stack = []
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }

    # Iterate through the string and check whether the current character is a closing bracket
        for c in s:
            if c in closeToOpen:

    # Check whether the stack is not empty and the last element on the stack is the corresponding opening bracket
                if stack and stack[-1] == closeToOpen[c]:

    # If so pop the last element on the stack
                    stack.pop()


                else:
                    return False

    # If the current character is not a closing bracket push it on the stack
            else:
                stack.append(c)

    # Return True if the stack is empty and False if not
        return True if not stack else False