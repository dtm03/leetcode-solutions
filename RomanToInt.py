# The goal is to convert a roman numeral to an integer => Use a dictionary

class Solution(object):
    def romanToInt(self, s):

        rom = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        prev, res = 0, 0

        for c in s:
            val = rom[c]
            res += val

            # If there is a smaller number in front of a bigger one (e.g. IV)
            if val > prev:
                # Substracts the previously added value and the same value again to account for the subtraction rule
                res -= 2 * prev
            prev = val
        return res

