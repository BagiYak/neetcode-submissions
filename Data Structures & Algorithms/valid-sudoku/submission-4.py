class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # Rows
        for row in board:
            nums = [x for x in row if x != "."]
            
            if len(nums) != len(set(nums)):
                return False

        # Columns
        for col in range(9):
            nums = []

            for row in range(9):
                value = board[row][col]

                if value != ".":
                    nums.append(value)

            if len(nums) != len(set(nums)):
                return False

        # 3x3 boxes
        for row in range(0, 9, 3):
            for col in range(0, 9, 3):

                nums = []

                for r in range(row, row + 3):
                    for c in range(col, col + 3):

                        value = board[r][c]

                        if value != ".":
                            nums.append(value)

                if len(nums) != len(set(nums)):
                    return False

        return True