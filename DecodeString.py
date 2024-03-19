# Example 1: Input: s = "3[a]2[bc]", Output: "aaabcbc";
# Example 2: Input: s = "2[abc]3[cd]ef", Output: "abcabccdcdcdef"

# The problem can be solved using a stack

class Solution(object):
    def decodeString(self, s):

        stack = []

        for c in s:
            # Until a closing brackets occurs all chars are pushed onto the stack
            if c != ']':
                stack.append(c)
            else:
                # All chars until are popped and added to a substring until an opening bracket occurs
                substr = ""
                while stack[-1] != "[":
                    substr = stack.pop() + substr
                stack.pop()

                # The substring is multiplied by the given number and pushed onto the stack again
                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k

                stack.append(int(k) * substr)

        return "".join(stack)