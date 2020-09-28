"""
给定一个二叉树，返回其节点值自底向上的层次遍历。 （即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）

例如：
给定二叉树 [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其自底向上的层次遍历为：

[
  [15,7],
  [9,20],
  [3]
]
"""
# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, x):
        self.right = None
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        results = [[root]]
        while len(results[-1]) > 0:
            result = []
            for node in results[-1]:
                if node.left:
                    result.append(node.left)
                if node.right:
                    result.append(node.right)
            results.append(result)
        real_results = []
        for result in results[:-1]:
            real_result = [i.val for i in result]
            real_results.insert(0, real_result)
        return real_results

if __name__ == '__main__':
    a = Solution()
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    b = a.levelOrderBottom(None)
    print(b)