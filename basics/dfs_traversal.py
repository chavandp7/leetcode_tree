from basics.TreeNode import TreeNode


class DFS_Traversal:
    def __init__(self, val: int, left: 'TreeNode' = None, right: 'TreeNode' = None) -> None:
        self.val = val
        self.left = left
        self.right = right

    # Root - Left - Right
    @staticmethod
    def preorder_dfs(root: 'TreeNode') -> None:
        if not root:
            return

        print(root.val, end=' ')
        DFS_Traversal.preorder_dfs(root.left)
        DFS_Traversal.preorder_dfs(root.right)

    # Left - Root - Right
    @staticmethod
    def inorder_dfs(root: 'TreeNode') -> None:
        if not root:
            return

        DFS_Traversal.inorder_dfs(root.left)
        print(root.val, end=' ')
        DFS_Traversal.inorder_dfs(root.right)

    # Root - Left - Right
    @staticmethod
    def postorder_dfs(root: 'TreeNode') -> None:
        if not root:
            return
        DFS_Traversal.postorder_dfs(root.left)
        DFS_Traversal.postorder_dfs(root.right)
        print(root.val, end=' ')


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

    print("preorder traversal")
    DFS_Traversal.preorder_dfs(root)
    print()

    print("inorder traversal")
    DFS_Traversal.inorder_dfs(root)
    print()

    print("postorder traversal")
    DFS_Traversal.postorder_dfs(root)
    print()
