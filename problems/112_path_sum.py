# Given the root of a binary tree and an integer targetSum,
# return true if the tree has a root-to-leaf path such that
# adding up all the values along the path equals targetSum.
#
# A leaf is a node with no children.

from typing import Optional

from basics.TreeNode import TreeNode


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        if not root.left and not root.right and targetSum == root.val:
            return True

        # if targetSum == root.val and (root.left or root.right):
        #     return False

        left_path = self.hasPathSum(root.left, targetSum - root.val)
        right_path = self.hasPathSum(root.right, targetSum - root.val)

        return left_path or right_path
