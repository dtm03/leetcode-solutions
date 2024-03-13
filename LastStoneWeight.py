import heapq
class Solution(object):
    def lastStoneWeight(self, stones):

        for i in range(len(stones)):
            stones[i] *= -1

        heapq.heapify(stones)

        while len(stones) > 1:
            s1 = heapq.heappop(stones)
            s2 = heapq.heappop(stones)
            result = s1 - s2
            if result != 0:
                heapq.heappush(stones, result)

        return -heapq.heappop(stones) if stones else 0