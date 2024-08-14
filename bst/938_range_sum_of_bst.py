# Given the root node of a binary search tree and two integers low and high,
# return the sum of values of all nodes with a value in the inclusive range [low, high].
from typing import Optional

from basics.TreeNode import TreeNode


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0

        sum = 0
        if low <= root.val and high >= root.val:
            sum += root.val

        if low < root.val:
            sum += self.rangeSumBST(root.left, low, high)

        if root.val < high:
            sum += self.rangeSumBST(root.right, low, high)

        return sum


if __name__ == "__main__":
    # root node
    root = TreeNode(10)

    # initialization
    node_one = TreeNode(5)
    node_two = TreeNode(15)

    node_three = TreeNode(3)
    node_four = TreeNode(7)

    node_five = TreeNode(18)

    # assignment
    root.left = node_one
    root.right = node_two

    node_one.left = node_three
    node_one.right = node_four

    node_two.right = node_five

    print("Range sum BST")
    print(Solution().rangeSumBST(root, 7, 15))
