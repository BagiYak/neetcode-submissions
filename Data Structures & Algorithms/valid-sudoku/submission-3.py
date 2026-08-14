import numpy as np

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        matrix = np.array(board)
        blocks = matrix.reshape(3, 3, 3, 3).swapaxes(1, 2)

        # Rows
        for row in matrix:
            nums = row[row != "."]
            if len(nums) != len(set(nums)):
                return False

        # Columns
        for col in matrix.T:
            nums = col[col != "."]
            if len(nums) != len(set(nums)):
                return False

        # 3x3 blocks
        for block_row in blocks:
            for block in block_row:
                nums = block[block != "."]
                if len(nums) != len(set(nums)):
                    return False

        return True
        