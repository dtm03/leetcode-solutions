class Solution(object):
    def wordPattern(self, pattern, s):
        words = s.split()
        if len(pattern) != len(words):
            return False

        c_to_w = {}

        for c, w in zip(pattern, words):
            if c in c_to_w:
                if c_to_w[c] != w:
                    return False
            else:
                if w in c_to_w.values():
                    return False
                c_to_w[c] = w

        return True