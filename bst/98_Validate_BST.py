# Given the root of a binary tree, determine if it is a valid binary search tree (BST).
#
# A valid BST is defined as follows:
#
#     The left
#     subtree
#     of a node contains only nodes with keys less than the node's key.
#     The right subtree of a node contains only nodes with keys greater than the node's key.
#     Both the left and right subtrees must also be binary search trees.
from typing import Optional

from basics.TreeNode import TreeNode


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root, min, max):
            if not root:
                return True

            if not (min < root.val < max):
                return False

            left = dfs(root.left, min, root.val)
            right = dfs(root.right, root.val, max)

            return left and right

        min = float("-inf")
        max = float("inf")

        return dfs(root, min, max)
