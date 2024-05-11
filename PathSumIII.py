class Solution(object):
    def pathSum(self, root, targetSum):
        def dfs(node, currentSum):
            if not node:
                return 0

            # Update the current sum with the value of the current node
            currentSum -= node.val

            # If we have found a valid path, increment the count
            count = 1 if currentSum == 0 else 0

            # Explore left and right subtrees, passing the updated current sum
            count += dfs(node.left, currentSum)
            count += dfs(node.right, currentSum)

            return count

        if not root:
            return 0

        # Start DFS from the root with an initial current sum of targetSum
        # root might be bigger than targetSum, so we need to explore the left and right subtrees
        return dfs(root, targetSum) + self.pathSum(root.left, targetSum) + self.pathSum(root.right, targetSum)