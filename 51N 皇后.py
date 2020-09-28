"""
n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。



上图为 8 皇后问题的一种解法。

给定一个整数 n，返回所有不同的 n 皇后问题的解决方案。

每一种解法包含一个明确的 n 皇后问题的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。

 

示例：

输入：4
输出：[
 [".Q..",  // 解法 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // 解法 2
  "Q...",
  "...Q",
  ".Q.."]
]
解释: 4 皇后问题存在两个不同的解法。
 

提示：

皇后彼此不能相互攻击，也就是说：任何两个皇后都不能处于同一条横行、纵行或斜线上。

"""

class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        执行用时：176 ms, 在所有 Python3 提交中击败了12.19%的用户
        内存消耗：14.3 MB, 在所有 Python3 提交中击败了5.75%的用户
        """
        result = []
        line = []
        for i in range(n):
            line.append(0)
        temp = []
        choices = []
        for i in range(n):
            temp.append(line.copy())
            choices.append(line.copy())
        c = 0
        while 0 <= c < n:
            potential_y = [int(i) for i in range(n) if choices[c][i] == 0]  # 对于所有没有使用过的y
            if len(potential_y) == 0:
                choices[c] = line.copy()
                temp[c - 1] = line.copy()
                c -= 1
                continue
            for yc in potential_y:  # 尝试棋子c可能的列号
                flag = True
                choices[c][yc] = 1
                for k in range(1, c + 1):  # 检查棋子c当前的位置是否与前边的冲突
                    if temp[c - k][yc] == 1:  # 存在冲突
                        flag = False
                        break  # 终止测试
                    if yc - k >= 0 and temp[c - k][yc - k] == 1:  # 存在冲突
                        flag = False
                        break  # 终止测试
                    if yc + k < n and temp[c - k][yc + k] == 1:  # 存在冲突
                        flag = False
                        break  # 终止测试
                if flag:  # 不存在冲突
                    temp[c][yc] = 1
                    if c != n - 1:  # 不是最后一个
                        c += 1
                    else:  # 是最后一个
                        result.append(temp.copy())
                        choices[c] = line.copy()
                        temp[c] = line.copy()
                        temp[c-1] = line.copy()
                        c -= 1  # 重新检测上一个棋子可能的位置
                    break
                elif yc == potential_y[-1]:  # 最后一个可行的也不可以
                    choices[c] = line.copy()
                    if c == 0:
                        c -= 1
                        break
                    temp[c-1] = line.copy()
                    c -= 1  # 有问题
        real_result = []
        for one_result in result:
            real_one_result = []
            for line in one_result:
                str_result = ''
                for c in line:
                    if c == 1:
                        str_result += 'Q'
                    else:
                        str_result += '.'
                real_one_result.append(str_result)
            real_result.append(real_one_result)
        return real_result

    def solveNQueens3(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        改进：将01标注的存储，改为数字存储使用和行号，减少内存消耗
        执行用时：180 ms, 在所有 Python3 提交中击败了11.63%的用户
        内存消耗：13.9 MB, 在所有 Python3 提交中击败了75.76%的用户
        """
        result = []
        temp = []
        choices = []
        for i in range(n):
            temp.append(-1)
            choices.append(-1)
        c = 0
        while 0 <= c < n:
            potential_y = [int(i) for i in range(choices[c]+1, n)]  # 对于所有没有使用过的y
            if len(potential_y) == 0:
                choices[c] = -1
                temp[c - 1] = -1
                c -= 1
                continue
            for yc in potential_y:  # 尝试棋子c可能的列号
                flag = True
                choices[c] = yc
                for k in range(1, c + 1):  # 检查棋子c当前的位置是否与前边的冲突
                    if temp[c - k] == yc:  # 存在冲突
                        flag = False
                        break  # 终止测试
                    if temp[c - k] == yc - k:  # 存在冲突
                        flag = False
                        break  # 终止测试
                    if temp[c - k] == yc + k:  # 存在冲突
                        flag = False
                        break  # 终止测试
                if flag:  # 不存在冲突
                    temp[c] = yc
                    if c != n - 1:  # 不是最后一个
                        c += 1
                    else:  # 是最后一个
                        result.append(temp.copy())
                        choices[c] = -1
                        temp[c] = -1
                        temp[c-1] = -1
                        c -= 1  # 重新检测上一个棋子可能的位置
                    break
                elif yc == potential_y[-1]:  # 最后一个可行的也不可以
                    choices[c] = -1
                    if c == 0:
                        c -= 1
                        break
                    temp[c-1] = -1
                    c -= 1  # 有问题
        return [["." * i + "Q" + "." * (n - i - 1) for i in sol] for sol in result]

    def solveNQueens2(self, n):
        def DFS(queens, xy_dif, xy_sum):
            p = len(queens)
            if p == n:
                result.append(queens)
                return
            for q in range(n):
                if q not in queens and p - q not in xy_dif and p + q not in xy_sum:
                    DFS(queens + [q], xy_dif + [p - q], xy_sum + [p + q])

        result = []
        DFS([], [], [])
        print(result)
        return [["." * i + "Q" + "." * (n - i - 1) for i in sol] for sol in result]


if __name__ == '__main__':
    a = Solution()
    n = 4
    b = a.solveNQueens3(n)
    print(b)