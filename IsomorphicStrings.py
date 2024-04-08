class Solution(object):
    def isIsomorphic(self, s, t):

        if len(s) != len(t):
            return False

        stmap = {}

        for i in range(len(s)):
            if s[i] in stmap.keys():
                if stmap[s[i]] != t[i]:
                    return False
            else:
                if t[i] in stmap.values():
                    return False
                stmap[s[i]] = t[i]

        return True