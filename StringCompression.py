class Solution(object):
    def compress(self, chars):
        if len(chars) < 2:
            return len(chars)

        l, r = 0, 0

        while r < len(chars):
            counter = 1
            while r < len(chars) - 1 and chars[r] == chars[r + 1]:
                counter += 1
                r += 1

            chars[l] = chars[r]
            l += 1

            if counter > 1:
                for val in str(counter):
                    chars[l] = val
                    l += 1

            r += 1

        return l