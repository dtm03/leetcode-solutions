class Solution(object):
    def addDigits(self, num):

        if num == 0:
            return 0
        elif num % 9 == 0:
            return 9
        else:
            return num % 9

'''
        l = [int(digit) for digit in str(num)]

        while len(l) > 1:
            l = [int(digit) for digit in str(num)]
            num = sum(l)
        
        return num
'''