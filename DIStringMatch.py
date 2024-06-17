class Solution(object):
    def diStringMatch(self, s):
        l, h = 0, len(s)
        res = []

        for c in s:
            if c == 'I':
                res.append(l)
                l += 1
            else:
                res.append(h)
                h -= 1

        res.append(l)

        return res

        