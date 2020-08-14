"""
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。

示例 1:

输入: "()"
输出: true
示例 2:

输入: "()[]{}"
输出: true
示例 3:

输入: "(]"
输出: false
示例 4:

输入: "([)]"
输出: false
示例 5:

输入: "{[]}"
输出: true
"""


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        while '{}' in s or '()'in s or '[]' in s:
            s = s.replace('{}', '')
            s = s.replace('()', '')
            s = s.replace('[]', '')
        return s == ''

    # def isValid(self, s):
    #     """
    #     :type s: str
    #     :rtype: bool
    #     """
    #     stack = []
    #     map = {'{':'}', '[':']', '(':')', '}':'', ']':'', ')':''}
    #     for word in s:
    #         if len(stack) == 0:
    #             stack = [word]
    #         elif map[stack[-1]] == word:
    #             stack = stack[:-1]
    #         else:
    #             stack.append(word)
    #     if len(stack) == 0:
    #         return True
    #     else:
    #         return False


if __name__ == '__main__':
    a = Solution()
    s = '()'
    b = a.isValid(s)
    print(b)