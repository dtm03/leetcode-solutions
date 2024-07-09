class Solution(object):
    def appendCharacters(self, s, t):
        pt, ps = 0, 0
        while pt < len(t) and ps < len(s):
            if s[ps] == t[pt]:
                pt += 1
            ps += 1
        return len(t) - pt