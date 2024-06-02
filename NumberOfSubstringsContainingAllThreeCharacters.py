class Solution(object):
    def numberOfSubstrings(self, s):
        res = 0
        left = 0
        counts = {'a': 0, 'b': 0, 'c': 0}

        for right, char in enumerate(s):
            counts[char] += 1

            while all(counts.values()):
                # If all characters 'a', 'b', and 'c' are present in the current window
                # increment the left pointer to find all substrings containing 'a', 'b', and 'c'
                counts[s[left]] -= 1
                left += 1

            # Add the count of substrings containing 'a', 'b', and 'c' for the current window
            # Since the left pointer moves one step further for each valid substring found,
            # the number of substrings is the difference between the current left pointer position and the starting position
            res += left

        return res