class Solution:
    def solveSudoku(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def isValid(row, col, val):
            if val in board[row]: return False
            for i in range(9):
                if val == board[i][col]: return False
            row_mod = 0
            if row >= 3:
                row_mod = 3
            if row >= 6:
                row_mod = 6

            col_mod = 0
            if col >= 3:
                col_mod = 3
            if col >= 6:
                col_mod = 6
            for i in range(3):
                for j in range(3):
                    if board[row_mod + i][col_mod + j] == val: return False
            return True

        # I want modified to function as a stack
        modified = []
        row = 0
        col = 0
        while row < 9:
            if col == 9:
                row += 1
                col = 0
                continue
            if len(modified) > 0:
                start, x, y = modified[-1]
                if row != x or col != y:
                    start = 1
                    backtracking = False
                else:
                    start += 1
                    backtracking = True
                    board[row][col] = "."
                    modified.pop()
            else:
                start = 1
                backtracking = False
            if not backtracking:
                if board[row][col] != ".":
                    col += 1
                    continue
            found = False
            for k in range(start, 10):
                if isValid(row, col, str(k)):
                    board[row][col] = str(k)
                    modified.append((k, row, col))
                    found = True
                    col += 1
                    break
            if not found:
                board[row][col] = "."
                if len(modified) == 0:
                    return
                row = modified[-1][1]
                col = modified[-1][2]

with open("input1.txt") as f:
    text = f.read()
    sudoku = []
    text = text.replace("[", "")
    text = text.replace("]", "")
    text = text.replace("\"", "")
    text = text.split(",")
    for i in range(9):
        row = []
        for j in range(9):
            row.append(text[i*9 + j])
        sudoku.append(row)
    solver = Solution
    solver.solveSudoku(solver, sudoku)
    print(sudoku)