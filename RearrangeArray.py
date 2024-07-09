class Solution(object):
    def rearrangeArray(self, nums):
        res = [None] * len(nums)
        pos_index, neg_index = 0, 1

        for n in nums:
            if n >= 0:
                res[pos_index] = n
                pos_index += 2
            else:
                res[neg_index] = n
                neg_index += 2

        return res
# Time: O(N)

# Slower but more intuitive solution:
# class Solution(object):
#     def rearrangeArray(self, nums):
#         pos, neg = [], []
#         for n in nums:
#             if n < 0:
#                 neg.append(n)
#             else:
#                 pos.append(n)
#
#         res = []
#
#         for i in range(len(pos)):
#             res.append(pos[i])
#             res.append(neg[i])
#
#         return res
