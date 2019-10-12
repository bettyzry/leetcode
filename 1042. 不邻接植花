class Solution:
    def gardenNoAdj(self, N: int, paths: List[List[int]]) -> List[int]:
        path = [[] for _ in range(N+1)]
        for x, y in paths:
            path[x].append(y)
            path[y].append(x)
        
        color = [0]*N
        for i in range(1, N+1):
            color[i-1] = ({1,2,3,4} - {color[j-1] for j in path[i]}).pop()
        return color                
