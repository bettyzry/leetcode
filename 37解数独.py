"""
编写一个程序，通过已填充的空格来解决数独问题。

一个数独的解法需遵循如下规则：

数字 1-9 在每一行只能出现一次。
数字 1-9 在每一列只能出现一次。
数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。
空白格用 '.' 表示。



一个数独。



答案被标成红色。

Note:

给定的数独序列只包含数字 1-9 和字符 '.' 。
你可以假设给定的数独只有唯一解。
给定数独永远是 9x9 形式的。
"""


class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """

        def get_potential(board, loc_i, loc_j):
            potential = [i for i in range(1, 10)]

            # 检查这一行中没有出现过的数字
            row = board[loc_i]
            for b in row:
                if isinstance(b, str) and b != '.' and int(b) in potential:
                    potential.remove(int(b))

            # 检查这一列中没有出现过的数字
            for row in board:
                if isinstance(row[loc_j], str) and row[loc_j] != '.' and int(row[loc_j]) in potential:
                    potential.remove(int(row[loc_j]))

            # 检查这个方块中没有出现过的数字
            b_i = int(loc_i / 3)
            b_j = int(loc_j / 3)
            for i in range(3):
                row = board[b_i * 3 + i]
                for j in range(3):
                    if isinstance(row[b_j * 3 + j], str) and row[b_j * 3 + j] != '.' and int(
                            row[b_j * 3 + j]) in potential:
                        potential.remove(int(row[b_j * 3 + j]))
            return potential

        def update_board(potentail_board, loc_i, loc_j, num):
            try_list = []
            num = int(num)
            # 检查这一行中没有出现过的数字
            row = potentail_board[loc_i]
            for j, b in enumerate(row):
                if isinstance(b, list) and num in b:
                    b.remove(num)
                    if len(b) == 1:
                        row[j] = str(b[0])
                        try_list.append([loc_i, j])

            # 检查这一列中没有出现过的数字
            for i, row in enumerate(potentail_board):
                if isinstance(row[loc_j], list) and num in row[loc_j]:
                    row[loc_j].remove(num)
                    if len(row[loc_j]) == 1:
                        row[loc_j] = str(row[loc_j][0])
                        try_list.append([i, loc_j])

            # 检查这个方块中没有出现过的数字
            b_i = int(loc_i / 3)
            b_j = int(loc_j / 3)
            for i in range(3):
                row = potentail_board[b_i * 3 + i]
                for j in range(3):
                    if isinstance(row[b_j * 3 + j], list) and num in row[b_j * 3 + j]:
                        row[b_j * 3 + j].remove(num)
                        if len(row[b_j * 3 + j]) == 1:
                            row[b_j * 3 + j] = str(row[b_j * 3 + j][0])
                            try_list.append([b_i * 3 + i, b_j * 3 + j])
                            potentail_board = update_board(board, b_i * 3 + i, b_j * 3 + j, (row[b_j * 3 + j][0]))
            return potentail_board

        def get_board(board, try_list):
            for [i, j] in try_list:
                potential = get_potential(board, i, j)  # 对第i,j个点确定他当前可能的值

        try_list = []
        for i, row in enumerate(board):
            for j, b in enumerate(row):
                if b == '.':
                    potential = get_potential(board, i, j)
                    if len(potential) == 1:
                        board[i][j] = str(potential[0])
                        board = update_board(board, i, j, potential[0])
                    else:
                        board[i][j] = potential
        return board

    def solveSudoku2(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """

        def get_potential(board, loc_i, loc_j):
            potential = [i for i in range(1, 10)]

            # 检查这一行中没有出现过的数字
            row = board[loc_i]
            for b in row:
                if isinstance(b, str) and b != '.' and int(b) in potential:
                    potential.remove(int(b))

            # 检查这一列中没有出现过的数字
            for row in board:
                if isinstance(row[loc_j], str) and row[loc_j] != '.' and int(row[loc_j]) in potential:
                    potential.remove(int(row[loc_j]))

            # 检查这个方块中没有出现过的数字
            b_i = int(loc_i / 3)
            b_j = int(loc_j / 3)
            for i in range(3):
                row = board[b_i * 3 + i]
                for j in range(3):
                    if isinstance(row[b_j * 3 + j], str) and row[b_j * 3 + j] != '.' and int(
                            row[b_j * 3 + j]) in potential:
                        potential.remove(int(row[b_j * 3 + j]))
            return potential

        def update_board(potentail_board, loc_i, loc_j, num):
            num = int(num)
            # 检查这一行中没有出现过的数字
            row = potentail_board[loc_i]
            for j, b in enumerate(row):
                if isinstance(b, list) and num in b:
                    b.remove(num)
                    if len(b) == 1:
                        row[j] = str(b[0])
                        potentail_board = update_board(board, loc_i, j, b[0])

            # 检查这一列中没有出现过的数字
            for i, row in enumerate(potentail_board):
                if isinstance(row[loc_j], list) and num in row[loc_j]:
                    row[loc_j].remove(num)
                    if len(row[loc_j]) == 1:
                        row[loc_j] = str(row[loc_j][0])
                        potentail_board = update_board(board, i, loc_j, row[loc_j][0])

            # 检查这个方块中没有出现过的数字
            b_i = int(loc_i / 3)
            b_j = int(loc_j / 3)
            for i in range(3):
                row = potentail_board[b_i * 3 + i]
                for j in range(3):
                    if isinstance(row[b_j * 3 + j], list) and num in row[b_j * 3 + j]:
                        row[b_j * 3 + j].remove(num)
                        if len(row[b_j * 3 + j]) == 1:
                            row[b_j * 3 + j] = str(row[b_j * 3 + j][0])
                            potentail_board = update_board(board, b_i * 3 + i, b_j * 3 + j, (row[b_j * 3 + j][0]))
            return potentail_board

        for i, row in enumerate(board):
            for j, b in enumerate(row):
                if b == '.':
                    potential = get_potential(board, i, j)
                    if len(potential) == 1:
                        board[i][j] = str(potential[0])
                        board = update_board(board, i, j, potential[0])
                    else:
                        board[i][j] = potential
        return board


if __name__ == '__main__':
    a = Solution()
    board = [[".", ".", "9", "7", "4", "8", ".", ".", "."], ["7", ".", ".", ".", ".", ".", ".", ".", "."],
             [".", "2", ".", "1", ".", "9", ".", ".", "."], [".", ".", "7", ".", ".", ".", "2", "4", "."],
             [".", "6", "4", ".", "1", ".", "5", "9", "."], [".", "9", "8", ".", ".", ".", "3", ".", "."],
             [".", ".", ".", "8", ".", "3", ".", "2", "."], [".", ".", ".", ".", ".", ".", ".", ".", "6"],
             [".", ".", ".", "2", "7", "5", "9", ".", "."]]
    b = a.solveSudoku2(board)
    print(b)
