# The time complexity of the above recursive solution is O(n), where n is the total number of nodes in the binary tree.
# The program requires O(h) extra space for the call stack, where h is the height of the tree.


def invertTree(root):
    if root is None:
        return None
    root.left, root.right = invertTree(root.right), invertTree(root.left)
    return root
