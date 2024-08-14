from collections import deque

from basics.dfs_traversal import TreeNode


def bfs_traversal(root: TreeNode) -> None:
    if not root:
        return

    queue = deque([root])

    while queue:
        nodes_at_current_level = len(queue)

        for i in range(nodes_at_current_level):
            node = queue.popleft()

            print(node.val, end=' ')

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

        print()
