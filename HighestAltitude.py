# Each element represents a change in altitude return the highest altitude -> Iterate through list and update the max

class Solution(object):
    def largestAltitude(self, gain):

    # Initialize variables for current altitude and max altitude
        alt = 0
        max = 0

    # Iterate through the list
        for e in gain:

    # Update the current altitude
            alt += e

    # Update the max altitude if it's smaller than the current one
            if alt > max:
                max = alt
            
        return max