class Solution(object):
    def summaryRanges(self, nums):
        if not nums:
            return []

        res = []
        start = end = nums[0]

        for num in nums[1:]:
            if num == end + 1:
                end = num
            else:
                if start == end:
                    res.append(str(start))
                else:
                    res.append(str(start) + "->" + str(end))
                start = end = num

        if start == end:
            res.append(str(start))
        else:
            res.append(str(start) + "->" + str(end))

        return res