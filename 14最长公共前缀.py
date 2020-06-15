class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        执行用时 :16 ms, 在所有 Python 提交中击败了93.64%的用户
        内存消耗 :12.7 MB, 在所有 Python 提交中击败了5.88%的用户
        """
        if len(strs) == 0:
            return ''
        common = strs[0]
        for str in strs[1:]:
            length = min(len(common), len(str))
            if common == str[:length]:
                continue
            else:
                i = 1
                while common[:i] == str[:i] and i <= length:
                    i += 1
                common = common[:i-1]
        return common

if __name__ == '__main__':
    a = Solution()
    t = a.longestCommonPrefix(["aa","a"])
    print(t)