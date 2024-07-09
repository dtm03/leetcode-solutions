class Solution(object):
    def isStrictlyPalindromic(self, n):
        def int_to_base(n, base):
            if n == 0:
                return '0'
            digits = []
            while n:
                digits.append(int(n % base))
                n //= base
            return ''.join(str(x) for x in digits[::-1])

        def is_palindromic(s):
            return s == s[::-1]

        for base in range(2, n - 1):
            base_representation = int_to_base(n, base)
            if not is_palindromic(base_representation):
                return False
        return True