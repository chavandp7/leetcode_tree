# Given the root of a Binary Search Tree (BST),
# return the minimum absolute difference between
# the values of any two different nodes in the tree.
from typing import Optional

from basics.TreeNode import TreeNode


class Solution:
    node_list = []

    def dfs(self, root: TreeNode):
        if not root:
            return -1

        self.dfs(root.left)
        self.node_list.append(root.val)
        self.dfs(root.right)

    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.dfs(root)

        min_diff = float('inf')
        # print(f"Inorder list - {self.node_list}")

        for i in range(1, len(self.node_list)):
            diff = self.node_list[i] - self.node_list[i - 1]
            min_diff = min(min_diff, diff)

        # print(f"min diff = {min_diff}")
        return min_diff


if __name__ == "__main__":
    root = TreeNode(1)

    zero = TreeNode(0)
    forty_eight = TreeNode(48)

    twelve = TreeNode(12)
    forty_nine = TreeNode(49)

    root.left = zero
    root.right = forty_eight

    forty_eight.left = twelve
    forty_eight.right = forty_nine

    Solution().getMinimumDifference(root)
