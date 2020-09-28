"""
给定一个二叉树，找出其最小深度。

最小深度是从根节点到最近叶子节点的最短路径上的节点数量。

说明: 叶子节点是指没有子节点的节点。

示例:

给定二叉树 [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回它的最小深度  2.
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        _min_ = 0
        _cur_min = 0
        ways = [root]
        while True:     # undo
            _cur_min += 1
            node = ways[-1]
            ways = ways[:-1]
            if node.right is not None:
                ways.append(node.right)
            if node.left is not None:    # 如果当前节点的左孩子不是空
                ways.append(node.left)

if __name__ == '__main__':
    a = Solution()
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    b = a.minDepth(root)
    print(b)