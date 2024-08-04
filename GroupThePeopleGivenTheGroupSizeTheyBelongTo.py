from collections import defaultdict


class Solution(object):
    def groupThePeople(self, groupSizes):

        # Dictionary to keep track of the groups being formed
        size_to_group = defaultdict(list)

        # Result list to store the final groups
        result = []

        # Iterate through each person and their group size
        for person, size in enumerate(groupSizes):
            size_to_group[size].append(person)

            # If the current group reaches its required size
            if len(size_to_group[size]) == size:
                result.append(size_to_group[size])
                # Clear the group to start forming a new one of the same size
                size_to_group[size] = []

        return result
