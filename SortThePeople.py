class Solution(object):
    def sortPeople(self, names, heights):
        # Combine names and heights into a list of tuples
        names_heights = list(zip(heights, names))

        # Sort the list of tuples by heights in descending order
        names_heights.sort(reverse=True, key=lambda x: x[0])

        # Extract the sorted names
        sorted_names = [name for height, name in names_heights]

        return sorted_names