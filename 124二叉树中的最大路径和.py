# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        return

if __name__ == '__main__':
    a = Solution()
    root = TreeNode(-10)
    root.left(TreeNode(9))
    root.right(TreeNode(20))
    root.right.left(TreeNode(15))
    root.right.right(TreeNode(7))
    path = a.maxPathSum(root)
    print(path)