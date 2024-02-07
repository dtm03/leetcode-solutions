# The goal is to reverse the vowels in a string => Use two pointers and swap if they are both pointing to vowels

class Solution(object):
    def reverseVowels(self, s):
        vows = "AEIOUaeiou"
        s = list(s)
        l, r = 0, len(s) - 1

        while (l < r):
            # The easiest way is to first look at the case where both aren't vowels
            if (s[l] not in vows):
                l+=1
            elif (s[r] not in vows):
                r-=1
            else:
                s[l], s[r] = s[r], s[l]
                l+=1
                r-=1

        return "".join(s)

    '''
    class Solution(object):
    def reverseVowels(self, s):
        vows = "AEIOUaeiou"
        s = list(s)  # Convert the string to a list to make it mutable
        l, r = 0, len(s) - 1

        while l < r:
            while l < r and s[l] not in vows:
                l += 1
            while l < r and s[r] not in vows:
                r -= 1

            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1

        return "".join(s)
    '''