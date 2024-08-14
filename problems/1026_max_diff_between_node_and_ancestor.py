from typing import Optional

from basics.TreeNode import TreeNode


class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def findMaxDiff(root: TreeNode, minimum: int, maximum: int) -> int:
            if not root:
                return 0

            val = root.val
            maximum = max(val, maximum)
            minimum = min(val, minimum)

            left_maximum_diff = findMaxDiff(root.left, minimum, maximum)
            right_maximum_diff = findMaxDiff(root.right, minimum, maximum)

            current_diff = maximum - minimum

            return max(left_maximum_diff, current_diff, right_maximum_diff)

        return findMaxDiff(root, root.val, root.val)
