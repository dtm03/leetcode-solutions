class Solution(object):
    def specialArray(self, nums):
        nums.sort(reverse=True)  # Sort nums in descending order
        n = len(nums)

        for i in range(n + 1):
            count = sum(1 for num in nums if num >= i)
            if count == i:
                return i
        return -1

# class Solution(object):
#     def specialArray(self, nums):
#          for j in range(max(nums) + 1):
#             curr = []
#             for i in range(len(nums)):
#                 if nums[i] >= j:
#                     curr.append(nums[i])
#             if len(curr) == j:
#                 return j
#         return -1