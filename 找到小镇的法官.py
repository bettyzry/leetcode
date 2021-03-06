class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        count = [0]*(N+1)
        for i, j in trust:
            count[i] = -1
            count[j] = count[j] + 1
        for i in range(1, len(count)):
            if count[i] == N-1:
                return i
        return -1
