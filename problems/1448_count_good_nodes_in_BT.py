from basics.TreeNode import TreeNode


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        stack = [(root, float("-inf"))]
        good_nodes = 0

        while stack:
            node, max_till_now = stack.pop()

            if node.val >= max_till_now:
                good_nodes += 1

            max_till_now = max(node.val, max_till_now)

            if node.left:
                stack.append((node.left, max_till_now))

            if node.right:
                stack.append((node.right, max_till_now))

        return good_nodes
