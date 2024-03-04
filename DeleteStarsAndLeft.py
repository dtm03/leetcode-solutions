class Solution(object):
    def removeStars(self, s):
        stack = []

        for c in s:
            if c == '*':
                if stack:  # Check if the stack is not empty
                    stack.pop()  # Remove the last non-star character
            else:
                stack.append(c)  # Push non-star characters onto the stack

        return ''.join(stack)