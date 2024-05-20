class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        sub = sum(arr[:k])
        counter = 1 if sub / k >= threshold else 0

        for i in range(k, len(arr)):
            sub += arr[i] - arr[i - k]
            if sub / k >= threshold:
                counter += 1

        return counter