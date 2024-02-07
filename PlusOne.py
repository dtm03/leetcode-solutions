# The goal ist to add one to the integer represented by the list.

class Solution(object):
    def plusOne(self, digits):
        digits.reverse()
        i = 0
        while digits[i] == 9:
            digits[i] = 0
            i+=1
            if i >= len(digits):
                digits.append(1)
                digits.reverse()
                return digits
        digits[i]+=1
        digits.reverse()
        return digits