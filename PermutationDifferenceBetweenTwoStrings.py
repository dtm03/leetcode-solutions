class Solution(object):
    def findPermutationDifference(self, s, t):
        res = 0
        for i in range(len(s)):
            for j in range(len(t)):
                if s[i] == t[j]:
                    res += abs(i - j)
        return res

## Faster solution:

    class Solution(object):
        def findPermutationDifference(self, s, t):
            s_positions = {}
            t_positions = {}

            # Store positions of each character in s
            for i, char in enumerate(s):
                if char in s_positions:
                    s_positions[char].append(i)
                else:
                    s_positions[char] = [i]

            # Store positions of each character in t
            for i, char in enumerate(t):
                if char in t_positions:
                    t_positions[char].append(i)
                else:
                    t_positions[char] = [i]

            res = 0

            # Calculate the difference using stored positions
            for char in s_positions:
                if char in t_positions:
                    s_pos_list = s_positions[char]
                    t_pos_list = t_positions[char]
                    for s_pos in s_pos_list:
                        for t_pos in t_pos_list:
                            res += abs(s_pos - t_pos)

            return res

        