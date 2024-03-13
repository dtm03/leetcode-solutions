from collections import Counter

class Solution(object):
    def canConstruct(self, ransomNote, magazine):

        ranC = Counter(ransomNote)
        magC = Counter(magazine)

        for c, count in ranC.items():
            if magC[c] < count:
                return False

        return True