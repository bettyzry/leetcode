"""
给定一个二叉树

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。

初始状态下，所有 next 指针都被设置为 NULL。

 

进阶：

你只能使用常量级额外空间。
使用递归解题也符合要求，本题中递归程序占用的栈空间不算做额外的空间复杂度。
 

示例：



输入：root = [1,2,3,4,5,null,7]
输出：[1,#,2,3,#,4,5,7,#]
解释：给定二叉树如图 A 所示，你的函数应该填充它的每个 next 指针，以指向其下一个右侧节点，如图 B 所示。
 

提示：

树中的节点数小于 6000
-100 <= node.val <= 100
"""


# Definition for a Node.
class Node:
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root):
        if root is None:
            return root
        if root.right is None and root.left is None:            # 都没
            return root
        elif root.left is not None and root.right is not None:    # 都有
            root.left.next = root.right
            root.right.next = self.getNext(root.next)
        elif root.left is not None and root.right is None:        # 左有，右none
            root.left.next = self.getNext(root.next)
        elif root.left is None and root.right is not None:        # 左none，右有
            root.right.next = self.getNext(root.next)
        self.connect(root.right)                                # 先写右侧的
        self.connect(root.left)
        return root

    def getNext(self, root):
        if root is None:
            return None
        if root.left is not None:
            return root.left
        if root.right is not None:
            return root.right
        if root.next is not None:
            return self.getNext(root.next)
        return None


if __name__ == '__main__':
    a = Solution()
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.right = Node(6)
    root.left.left.left = Node(7)
    root.right.right.right = Node(8)
    b = a.connect(root)
    print(b)