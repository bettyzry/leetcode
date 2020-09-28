"""

请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。
例如，字符串"+100"、"5e2"、"-123"、"3.1416"、"-1E-16"、"0123"都表示数值，但"12e"、"1a3.14"、"1.2.3"、"+-5"及"12e+5.4"都不是。
Wrong: 1e1e1, 1e1E, 1.1.1, 1.1e1.1, +1+1, 1e, -e, .e, ., -, 1a, .+1
"""


class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        import re

        def check(s, isfirst):
            if len(s) == 0:
                return False
            if len(s) == 1:
                if s > '9' or s < '0':
                    return False
            if not isfirst and '.' in s:
                return False
            if s.count('+') > 1:
                return False
            if s.count('-') > 1:
                return False
            if s.count('.') > 1:
                return False

            pre = s[0]
            for i in s[1:]:
                if pre == '+' or pre == '-' or pre == '.':
                    if '0' <= i <= '9' or i =='.':
                        pre = i
                    else:
                        return False
                elif '0' <= pre <= '9':
                    if '0' <= i <= '9' or i == '.':
                        pre = i
                    else:
                        return False
                else:
                    return False
            return True

        while len(s) > 0 and s[0] == ' ':
            s = s[1:]
        while len(s) > 0 and s[-1] == ' ':
            s = s[:-1]
        if len(s) == 0:
            return False


        if ' ' in s:
            return False
        snew = re.split('[eE]', s)
        if len(snew) == 1:
            return check(snew[0], True)
        elif len(snew) == 2:
            return check(snew[0], True) and check(snew[1], False)
        else:
            return False


if __name__ == '__main__':
    a = Solution()
    s = "-."
    b = a.isNumber(s)
    print(b)
