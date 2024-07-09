class Solution(object):
    def threeConsecutiveOdds(self, arr):
        odds = 0
        for e in arr:
            if e % 2 == 1:
                odds += 1
                if odds == 3:
                    return True
            else:
                odds = 0
        return False