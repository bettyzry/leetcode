# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str 'a,b,c,d,e'
        执行用时 : 1792 ms, 在所有 Python3 提交中击败了5.23%的用户
        内存消耗 : 18.4 MB, 在所有 Python3 提交中击败了50.00%的用户
        """
        if not root:
            return []
        l = []
        que = [root]
        while que:
            node = que[0]
            que = que[1:]
            if node:
                l.append(node.val)
                que.append(node.left)
                que.append(node.right)
            else:
                l.append(None)
        return l

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str 'a,b,c,d,e'
        :rtype: TreeNode
        """
        datalist = data
        if len(datalist) == 0:
            return []
        root = TreeNode(datalist[0])
        datalist = datalist[1:]
        que = [root]
        while que:
            if not datalist:
                return root
            node = que[0]
            que = que[1:]
            if datalist[0] != None:
                node.left = TreeNode(datalist[0])
                que.append(node.left)
            datalist = datalist[1:]
            if datalist[0]:
                node.right = TreeNode(datalist[0])
                que.append(node.right)
            datalist = datalist[1:]
        return root



# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

if __name__ == '__main__':
    tree = TreeNode('-1')
    tree.left = TreeNode('0')
    tree.right = TreeNode('1')
    a = Codec()
    b = a.serialize(tree)
    print(b)
    c = a.deserialize([-1,0,1])
    print(c)
