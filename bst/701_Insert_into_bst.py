# You are given the root node of a binary search tree (BST)
# and a value to insert into the tree. Return the root node of the BST after the insertion.
# It is guaranteed that the new value does not exist in the original BST.
#
# Notice that there may exist multiple valid ways for the insertion,
# as long as the tree remains a BST after insertion. You can return any of them.
from typing import Optional

from basics.TreeNode import TreeNode


class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def insert(parent: TreeNode, root: TreeNode, val: int, dir: str):
            if not root:
                root = TreeNode(val)
                if dir == 'left':
                    parent.left = root
                else:
                    parent.right = root
                return

            if val < root.val:
                insert(root, root.left, val, 'left')
            else:
                insert(root, root.right, val, 'right')

        if not root:
            root = TreeNode(val)
            return root
        insert(root, root, val, 'left')
        return root
