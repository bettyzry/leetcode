class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        head = 0
        tail = len(s) - 1
        while head <= tail:
            if (s[head] > 'z' or s[head] < 'a') and (s[head] > '9' or s[head] < '0'):
                head += 1
            elif (s[tail] > 'z' or s[tail] < 'a') and (s[tail] > '9' or s[tail] < '0'):
                tail -= 1
            elif s[head] == s[tail]:
                head += 1
                tail -= 1
            else:
                return False
        return True



if __name__ == '__main__':
    a = Solution()
    s = "00"
    root = a.isPalindrome(s)
    print(root)