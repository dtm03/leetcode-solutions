# The goal is to decide if we can plant n flowers in a flowerbed. The flowerbed is represented as an array of 0 and 1,
# where 0 means empty and 1 means planted. Two flowers cannot be planted next to each other.
# => Add 0s to the beginning and end of the array to avoid edge cases.

class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):

        # Add 0s to the beginning and end of the array
        f = [0] + flowerbed + [0]

        # Iterates through the array neglecting the added zeroes
        for i in range(1, len(f) - 1):

            # Checks whether the current position and its neighbors are empty
            if f[i-1] == 0 and f[i] == 0 and f[i+1] == 0:

                # Plants a flower (important for the next iteration)
                f[i] = 1

                # Decreases the number of flowers to plant
                n-=1
                
        return n <= 0