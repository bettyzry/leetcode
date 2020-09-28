"""
让我们一起来玩扫雷游戏！

给定一个代表游戏板的二维字符矩阵。 'M' 代表一个未挖出的地雷，'E' 代表一个未挖出的空方块，'B' 代表没有相邻（上，下，左，右，和所有4个对角线）地雷的已挖出的空白方块，数字（'1' 到 '8'）表示有多少地雷与这块已挖出的方块相邻，'X' 则表示一个已挖出的地雷。

现在给出在所有未挖出的方块中（'M'或者'E'）的下一个点击位置（行和列索引），根据以下规则，返回相应位置被点击后对应的面板：

如果一个地雷（'M'）被挖出，游戏就结束了- 把它改为 'X'。
如果一个没有相邻地雷的空方块（'E'）被挖出，修改它为（'B'），并且所有和其相邻的未挖出方块都应该被递归地揭露。
如果一个至少与一个地雷相邻的空方块（'E'）被挖出，修改它为数字（'1'到'8'），表示相邻地雷的数量。
如果在此次点击中，若无更多方块可被揭露，则返回面板。
 

示例 1：

输入:

[['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'M', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E']]

Click : [3,0]

输出:

[['B', '1', 'E', '1', 'B'],
 ['B', '1', 'M', '1', 'B'],
 ['B', '1', '1', '1', 'B'],
 ['B', 'B', 'B', 'B', 'B']]

解释:

示例 2：

输入:

[['B', '1', 'E', '1', 'B'],
 ['B', '1', 'M', '1', 'B'],
 ['B', '1', '1', '1', 'B'],
 ['B', 'B', 'B', 'B', 'B']]

Click : [1,2]

输出:

[['B', '1', 'E', '1', 'B'],
 ['B', '1', 'X', '1', 'B'],
 ['B', '1', '1', '1', 'B'],
 ['B', 'B', 'B', 'B', 'B']]

解释:

 

注意：

输入矩阵的宽和高的范围为 [1,50]。
点击的位置只能是未被挖出的方块 ('M' 或者 'E')，这也意味着面板至少包含一个可点击的方块。
输入面板不会是游戏结束的状态（即有地雷已被挖出）。
简单起见，未提及的规则在这个问题中可被忽略。例如，当游戏结束时你不需要挖出
"""


class Solution(object):
    def updateBoard(self, board, click):
        # --------------- 计算最终的board ----------------- #
        new_board = []
        for y in range(len(board)):
            line = []
            for x in range(len(board[0])):
                line.append('0')
            new_board.append(line)
        for y in range(len(board)):
            for x in range(len(board[0])):
                if board[y][x] == 'M':
                    new_board[y][x] = 'X'
                    steps = [[1, 1], [1, 0], [1, -1], [0, 1], [0, -1], [-1, 1], [-1, 0], [-1, -1]]
                    for step in steps:
                        loc_y = y + step[0]
                        loc_x = x + step[1]
                        if 0 <= loc_y < len(board) and 0 <= loc_x < len(board[0]):
                            if new_board[loc_y][loc_x] == 'X':
                                continue
                            else:
                                new_board[loc_y][loc_x] = str(int(new_board[loc_y][loc_x]) + 1)

        # ---------------- 计算此次点击对应的board ----------------- #
        def loop(b, c):
            y = len(b)
            x = len(b[0])
            if new_board[c[0]][c[1]] == 'X':
                b[c[0]][c[1]] = 'X'
                return b
            elif 0 < int(new_board[c[0]][c[1]]) <= 9:
                b[c[0]][c[1]] = new_board[c[0]][c[1]]
                return b
            elif new_board[c[0]][c[1]] == '0':
                b[c[0]][c[1]] = 'B'
                steps = [[1, 1], [1, 0], [1, -1], [0, 1], [0, -1], [-1, 1], [-1, 0], [-1, -1]]
                for step in steps:
                    loc_y = c[0] + step[0]
                    loc_x = c[1] + step[1]
                    if 0 <= loc_y < y and 0 <= loc_x < x and b[loc_y][loc_x] == 'E':
                        b = loop(b, [loc_y, loc_x])
            return b
        return loop(board, click)


if __name__ == '__main__':
    a = Solution()
    board = [['B', '1', 'E', '1', 'B'],
 ['B', '1', 'M', '1', 'B'],
 ['B', '1', '1', '1', 'B'],
 ['B', 'B', 'B', 'B', 'B']]
    click = [3, 0]
    board = a.updateBoard(board, click)
    print(board)