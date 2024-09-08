class Solution(object):
    def findArray(self, pref):
        res = [pref[0]]
        for i in range(1, len(pref)):
            res.append(pref[i] ^ pref[i-1])
        return res