# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return None
        invert_root = TreeNode(root.val)
        inver_nodes = [invert_root]
        nodes = [root]
        while nodes:
            node = nodes[0]
            nodes = nodes[1:]
            invert_node = inver_nodes[0]
            inver_nodes = inver_nodes[1:]
            if node.right is not None:
                nodes.append(node.right)
                invert_node.left = TreeNode(node.right.val)
                inver_nodes.append(invert_node.left)
            if node.left is not None:
                nodes.append(node.left)
                invert_node.right = TreeNode(node.left.val)
                inver_nodes.append(invert_node.right)
        return invert_root


if __name__ == '__main__':
    a = Solution()
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(9)
    b = a.invertTree(root)
    print(b)