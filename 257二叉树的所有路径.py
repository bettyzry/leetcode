"""
给定一个二叉树，返回所有从根节点到叶子节点的路径。

说明: 叶子节点是指没有子节点的节点。

示例:

输入:

   1
 /   \
2     3
 \
  5

输出: ["1->2->5", "1->3"]

解释: 所有根节点到叶子节点的路径为: 1->2->5, 1->3
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """

        def path_to_str(path):
            p = str(path[0])
            for i in path[1:]:
                p += '->'
                p += str(i)
            return p

        def DFS(n, path):
            path.append(n.val)
            if n.right is None and n.left is None:
                p = path_to_str(path)
                result.append(p)
                return path[:-1]
            if n.left is not None:
                path = DFS(n.left, path)
            if n.right is not None:
                path = DFS(n.right, path)
            return path[:-1]

        result = []
        if root is None:
            return []
        else:
            DFS(root, [])
        return result

if __name__ == '__main__':
    a = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.right = TreeNode(5)
    root.right = TreeNode(3)
    b = a.binaryTreePaths(root)
    print(b)
