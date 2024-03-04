# Update the pointer pointing to the smaller element in order to maximize the area

class Solution(object):
    def maxArea(self, height):

        l, r = 0, len(height) - 1
        res = 0

        while l < r:
            curr = (r - l) * min(height[l], height[r])
            res = max(curr, res)
            if height[l] > height[r]:
                r-=1
            else:
                l+=1

        return res