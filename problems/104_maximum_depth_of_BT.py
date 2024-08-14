# Given the root of a binary tree, return its maximum depth.
#
# A binary tree's maximum depth is the number of nodes along the
# longest path from the root node down to the farthest leaf node.

from basics.dfs_traversal import TreeNode


def maxDepth(root: TreeNode) -> int:
    if not root:
        return 0

    left_depth = maxDepth(root.left)
    right_depth = maxDepth(root.right)

    return 1 + max(left_depth, right_depth)


if __name__ == "__main__":
    # root node
    root = TreeNode(0)

    # initialization
    one = TreeNode(1)
    two = TreeNode(2)

    three = TreeNode(3)
    four = TreeNode(4)

    five = TreeNode(5)
    six = TreeNode(6)

    # assignment
    root.left = one
    root.right = two

    one.left = three
    one.right = four

    two.right = five
    four.right = six

    print("maximum depth of the tree {}".format(maxDepth(root)))
