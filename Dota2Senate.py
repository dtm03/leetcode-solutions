from collections import deque

# The trick is to work with two separate Queue's
class Solution(object):
    def predictPartyVictory(self, senate):
        senate = list(senate)
        D, R = deque(), deque()

        for i, c in enumerate(senate):
            if c == 'R':
                R.append(i)
            else:
                D.append(i)

        while R and D:
            if R[0] < D[0]:
                D.popleft()
                R.append(R[0] + len(senate))
                R.popleft()
            else:
                R.popleft()
                D.append(D[0] + len(senate))
                D.popleft()

        if R:
            return "Radiant"
        else:
            return "Dire"