class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def recoverFromPreorder(self, S):
        """
        :type S: str
        :rtype: TreeNode
        执行用时：64 ms, 在所有 Python3 提交中击败了100.00%的用户
        内存消耗：14.4 MB, 在所有 Python3 提交中击败了100.00%的用户
        """
        data = S.split('-')
        root = TreeNode(data[0])
        dic = {0: root}
        depth = 1
        for s in data[1:]:
            if s == '':
                depth += 1
            else:
                node = TreeNode(s)
                dic[depth] = node
                if not dic[depth - 1].left:
                    dic[depth - 1].left = node
                else:
                    dic[depth - 1].right = node
                depth = 1
        return dic[0]




if __name__ == '__main__':
    a = Solution()
    s = "10"
    root = a.recoverFromPreorder(s)
    print(root)