The projects in this file are solutions I submitted on Leetcode for question 37: [Sudoku Solver](https://leetcode.com/problems/sudoku-solver/description/).
# RecSolution.py
[My submission](https://leetcode.com/problems/sudoku-solver/submissions/1331048009)

As the name of the file suggests, I first made a recursive solution. My solution follows a depth first search approach where it considers one tile in the sudoku for
each recursive call. I felt a depth first search approach was most appropriate in this instance to minimize the memory used during computation. If needed, this
solution could be adapted to find all possible solutions while still using a depth first search by creating a List to hold completed sudoku boards and creating a
deep copy of the board whenever a solution is found. A quick sample of what that might look like can be seen here:
```
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> List[List[List[str]]]:
        """
        Will now return a list of all feasible boards for a given input
        """
            
        def isValid(row: int, col: int, val: int):
            if val in board[row]: return False
            for i in range(9):
                if board[i][col] == val: return False
            for i in range(3):
                for j in range(3):
                    if board[row//3 * 3 + i][col//3 * 3 + j] == val: return False
            return True
        
        def recSolve(row, col):
            if col == 9: return recSolve(row+1, 0)
            if row == 9: return True
            if board[row][col] != ".": return recSolve(row, col+1)
            for k in range(1, 10):
                if isValid(row, col, str(k)):
                    board[row][col] = str(k)
                    if recSolve(row, col+1):
                      all_solutions.append(board.copy())
                      return False
            board[row][col] = "."
            return False

        all_solutions = []
        recSolve(0, 0)
        return all_solutions
```
Please note that this proposed code has not been tested as of now.

# BottomUpSolution.py
[My submission](https://leetcode.com/problems/sudoku-solver/submissions/1334586129)

As a personal challenge and attempt to improve the runtime of my recursive solution, I attempted to create a solution that would
make no recursive calls. I thought that by performing all calculations in the same function call instead of creating a potentially
massive call tree, the system would be able to perform the calculations faster.

To my dissapointment, this solution was only 2ms faster in completing the LeetCode tests than my recursive solution.
While dissapointing given the amount of time it took to debug this solution, I am very proud of my ability to adapt my code.
In theory, using this kind of solution should be much better if I wanted to convert this code to a language like C which doesn't
handle recursion as well as Python does.

# Input files explained
It should be noted that input2.txt is not solvable. It was simply used to debug the bottom up solution's backtracking.
