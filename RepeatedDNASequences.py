# Slding window approach

class Solution(object):
    def findRepeatedDnaSequences(self, s):
        seqs = set()
        repeated_seqs = set()
        i = 10
        while i <= len(s):
            current_seq = s[i - 10:i]
            if current_seq in seqs:
                repeated_seqs.add(current_seq)
            else:
                seqs.add(current_seq)
            i += 1

        return list(repeated_seqs)