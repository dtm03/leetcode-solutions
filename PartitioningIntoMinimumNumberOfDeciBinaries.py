class Solution(object):
    def minPartitions(self, n):
        return int(sorted(n)[-1])