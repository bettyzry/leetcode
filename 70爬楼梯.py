class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        ############## way1 ################
        """
        time:   68ms 7.43%
        memory: 28.1M 6.67%
        """
        # from scipy.special import comb
        # count = 0
        # for i in range(int(n/2)+1):
        #     count += comb(n-i, i)
        # return int(count)

        ############## way2 #################
        """
        超时
        """
        # if n>2:
        #     return self.climbStairs(n-1) + self.climbStairs(n-2)
        # else:
        #     return n

        ############## way3 ################
        """
        time:   20ms 66.55%
        memory: 12.6M 6.67%
        """
        from math import sqrt
        if n < 2:
            return n
        an_1 = 1
        an_2 = 2
        an = 0
        for i in range(2, n):
            an = an_1+an_2
            an_1 = an_2
            an_2 = an
        return an


if __name__ == '__main__':
    a = Solution()
    t = a.climbStairs(6)
    print(t)