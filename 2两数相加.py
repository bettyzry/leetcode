"""

给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：

输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807
"""
# Definition for singly-linked list.


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        l = ListNode(0)
        cur_l = l
        c = 0
        while l1 and l2:
            re = l1.val + l2.val+c
            num = re - re//10*10
            c = re//10
            cur_l.next = ListNode(num)
            cur_l = cur_l.next
            l1 = l1.next
            l2 = l2.next
        while l1:
            re = l1.val + c
            num = re - re // 10 * 10
            c = re // 10
            cur_l.next = ListNode(num)
            cur_l = cur_l.next
            l1 = l1.next
        while l2:
            re = l2.val+c
            num = re - re//10*10
            c = re//10
            cur_l.next = ListNode(num)
            cur_l = cur_l.next
            l2 = l2.next
        if c:
            cur_l.next = ListNode(c)
        return l.next

    def addTwoNumbers2(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        执行用时：52 ms, 在所有 Python 提交中击败了98.20%的用户
        内存消耗：12.5 MB, 在所有 Python 提交中击败了54.13%的用户
        """
        num_1 = 0
        count_1 = 0
        num_2 = 0
        count_2 = 0
        while l1:
            num_1 += l1.val*10**count_1
            l1 = l1.next
            count_1 += 1
        while l2:
            num_2 += l2.val * 10 ** count_2
            l2 = l2.next
            count_2 += 1
        num = num_1 + num_2
        l = ListNode(num - num//10*10)
        cur_l = l
        num = int(num/10)
        while num:
            part_num = num - num//10*10
            cur_l.next = ListNode(part_num)
            cur_l = cur_l.next
            num = int(num / 10)
        return l


if __name__ == '__main__':
    a = Solution()
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)
    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)
    b = a.addTwoNumbers(l1, l2)
    print(b)