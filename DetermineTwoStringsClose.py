from collections import Counter

# Two strings are closed if you can swap characters or transform an existing character into another one
# and get the other String

class Solution(object):
    def closeStrings(self, word1, word2):

        c1 = Counter(word1)
        c2 = Counter(word2)

        # This counts the frequencies
        n1 = Counter([v for v in c1.values()])
        n2 = Counter([v for v in c2.values()])

        return c1 == c2 or (n1 == n2 and set(word1) == set(word2))