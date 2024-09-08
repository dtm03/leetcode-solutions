class Solution(object):
    def maxDistance(self, arrays):
        max_distance = 0

        # Initialize the first array's min and max as the starting points
        min_val = arrays[0][0]
        max_val = arrays[0][-1]

        # Loop through the rest of the arrays starting from the second one
        for i in range(1, len(arrays)):
            current_min = arrays[i][0]
            current_max = arrays[i][-1]

            # Calculate the distance using the current array's min and max
            max_distance = max(max_distance, abs(max_val - current_min), abs(current_max - min_val))

            # Update the global min and max using the current array's values
            min_val = min(min_val, current_min)
            max_val = max(max_val, current_max)

        return max_distance
        