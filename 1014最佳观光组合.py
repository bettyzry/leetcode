class Solution:
    # def maxScoreSightseeingPair(self, A):
    #     '''
    #     超时
    #     '''
    #     _max_ = 0
    #     for i in range(len(A)-1):
    #         for j in range(i+1, len(A)):
    #             _max_ = max(_max_, A[i]+A[j]+i-j)
    #     return _max_

    # def maxScoreSightseeingPair(self, A):
    #     '''
    #     没有pandas的包
    #     '''
    #     from pandas import Series
    #     A = Series(A)
    #     A = A.sort_values(ascending=False)
    #     index = list(A.index)
    #     A = A.values
    #     _max_ = 0
    #     for i in range(len(A) - 1):
    #         for j in range(i + 1, len(A)):
    #             if A[i] + A[j] <= _max_:
    #                 break
    #             _max_ = max(_max_, A[i] + A[j] - abs(index[i] - index[j]))
    #     return _max_

    # def maxScoreSightseeingPair(self, A):
    #     '''
    #     超时
    #     '''
    #     import numpy as np
    #     A = np.array(A)
    #     index = A.argsort()
    #     A.sort()
    #     _max_ = A[-1] + A[-2] - abs(index[-1]-index[-2])
    #     for i in range(len(A) - 1, 1, -1):
    #         for j in range(i-1, 0, -1):
    #             if A[i] + A[j] <= _max_:
    #                 break
    #             _max_ = max(_max_, A[i] + A[j] - abs(index[i] - index[j]))
    #     return _max_
    # def maxScoreSightseeingPair(self, A):
    #     '''
    #     超时
    #     '''
    #     _max_ = 0
    #     for i in range(len(A)-1):
    #         a = [A[j] - j + i for j in range(i+1, len(A))]
    #         _max_ = max(_max_, A[i] + max(a))
    #     return _max_

    def maxScoreSightseeingPair(self, A):
        '''
        执行用时 :472 ms, 在所有 Python 提交中击败了66.67%的用户
        内存消耗 :17.4 MB, 在所有 Python 提交中击败了100.00%的用户
        '''
        Aj = [0]*len(A)
        Aj[len(A)-1] = A[len(A)-1]-len(A)+1
        for j in range(len(A)-2, 0, -1):
            Aj[j] = max(A[j]-j, Aj[j+1])
        _max_ = A[0] + Aj[1]
        for i in range(1, len(A)-1):
            _max_ = max(_max_, A[i] + i + Aj[i+1])
        return _max_

if __name__ == '__main__':
    a = Solution()
    l = [1,3,5]
    result = a.maxScoreSightseeingPair(l)
    print(result)
