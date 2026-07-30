# Valid Sudoku
# You are given a 9 x 9 Sudoku board board. A Sudoku board is valid if the following rules are followed:

# Each row must contain the digits 1-9 without duplicates.
# Each column must contain the digits 1-9 without duplicates.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without duplicates.
# Return true if the Sudoku board is valid, otherwise return false

# Note: A board does not need to be full or be solvable to be valid.

# Example 1:
# Input: board =
# [["1","2",".",".","3",".",".",".","."],
#  ["4",".",".","5",".",".",".",".","."],
#  [".","9","8",".",".",".",".",".","3"],
#  ["5",".",".",".","6",".",".",".","4"],
#  [".",".",".","8",".","3",".",".","5"],
#  ["7",".",".",".","2",".",".",".","6"],
#  [".",".",".",".",".",".","2",".","."],
#  [".",".",".","4","1","9",".",".","8"],
#  [".",".",".",".","8",".",".","7","9"]]

# Output: true

# Example 2:

# Input: board =
# [["1","2",".",".","3",".",".",".","."],
#  ["4",".",".","5",".",".",".",".","."],
#  [".","9","1",".",".",".",".",".","3"],
#  ["5",".",".",".","6",".",".",".","4"],
#  [".",".",".","8",".","3",".",".","5"],
#  ["7",".",".",".","2",".",".",".","6"],
#  [".",".",".",".",".",".","2",".","."],
#  [".",".",".","4","1","9",".",".","8"],
#  [".",".",".",".","8",".",".","7","9"]]

# Output: false

# Explanation: There are two 1's in the top-left 3x3 sub-box.

# Constraints:

# board.length == 9
# board[i].length == 9
# board[i][j] is a digit 1-9 or '.'.

# You should aim for a solution as good or better than
# O(n^2) time and O(n^2) space,
# where n is the number of rows in the square grid.

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        mSet = [set() for _ in range(9)]
        mBox = [set() for _ in range(9)]
        k = 1
        x = 1

        for i, row in enumerate(board):

            rSet = set()
            
            if x * 3 == i:
                x = x + 1

            for j, item in enumerate(row):

                if item == '.':
                    continue

                # Box
                box = (i // 3) * 3 + (j // 3)

                if item in mBox[box]:
                    return False
                else:
                    mBox[box].add(item)

                if j == 8:
                    k = 1

                # Row
                if item in rSet:
                    return False
                else:
                    rSet.add(item)

                # Column
                if item in mSet[j]:
                    return False
                else:
                    mSet[j].add(item)
            
        return True

# spent 1 hour and 52 min
# got in 2 given cases: 1 case error 2 case ok
# asked ChatGPT review my code for logic erros and bugs and after that fixed to success result
# broken code:

# class Solution:
#     def isValidSudoku(self, board: List[List[str]]) -> bool:

#         rSet = set()
#         mSet = [set() for _ in range(9)]
#         mBox = [set() for _ in range(9)]
#         k = 1
#         x = 1

#         for i, row in enumerate(board):
            
#             if x * 3 == i:
#                 x = x + 1

#             for j, item in enumerate(row):

#                 # Box
#                 if k * 3 == j:
#                     k = k + 1

#                 if  item != '.' and item in mBox[k*x]:
#                     return False
#                 else:
#                     mBox[k*x].add(item)

#                 if j == 8:
#                     k = 1

#                 # Row
#                 if item != '.' and item in rSet:
#                     return False
#                 else:
#                     rSet.add(item)

#                 # Column
#                 if item != '.' and item in mSet[i]:
#                     return False
#                 else:
#                     mSet[i].add(item)
            
#         return True