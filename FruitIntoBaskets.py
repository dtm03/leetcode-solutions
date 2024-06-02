class Solution(object):
    def totalFruit(self, fruits):
        fc = {}
        l = 0
        res = 0

        for r, f in enumerate(fruits):
            fc[f] = fc.get(f, 0) + 1

            while len(fc) > 2:
                fc[fruits[l]] -= 1
                if fc[fruits[l]] == 0:
                    del fc[fruits[l]]
                l += 1

            res = max(res, r - l + 1)

        return res