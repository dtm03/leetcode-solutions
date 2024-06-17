class Solution(object):
    def reverseOnlyLetters(self, s):
        # Convert the string to a list of characters for mutability
        s = list(s)

        l, r = 0, len(s) - 1

        while l < r:
            # Move l to the right until we find a letter
            while l < r and not s[l].isalpha():
                l += 1
            # Move r to the left until we find a letter
            while l < r and not s[r].isalpha():
                r -= 1

            # Swap the letters at l and r
            if l < r:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1

        # Convert the list of characters back to a string
        return "".join(s)
