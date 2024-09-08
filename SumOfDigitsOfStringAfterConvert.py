import string

class Solution(object):
    def getLucky(self, s, k):
        # Mapping alphabet characters to their positions (1-based index)
        alpha_dic = {letter: str(index) for index, letter in enumerate(string.ascii_lowercase, start=1)}

        # Convert the string to a numeric string based on the alphabet position
        res = ''.join(alpha_dic[c] for c in s)

        # Sum the digits of the numeric string k times
        for _ in range(k):
            res = str(sum(int(digit) for digit in res))

        return int(res)