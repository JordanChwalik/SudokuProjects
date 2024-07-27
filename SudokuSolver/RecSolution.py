class Solution:
    def solveSudoku(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def isValid(row: int, col: int, val: int):
            if val in board[row]: return False
            for i in range(9):
                if board[i][col] == val: return False
            for i in range(3):
                for j in range(3):
                    if board[row // 3 * 3 + i][col // 3 * 3 + j] == val: return False
            return True

        def recSolve(row, col):
            if col == 9: return recSolve(row + 1, 0)
            if row == 9: return True
            if board[row][col] != ".": return recSolve(row, col + 1)
            for k in range(1, 10):
                if isValid(row, col, str(k)):
                    board[row][col] = str(k)
                    if recSolve(row, col + 1): return True
            board[row][col] = "."
            return False

        recSolve(0, 0)
        return

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