import collections
from typing import List
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Time complexity: O(9^2)
        # Dictionaries with set values, keys are row val/col val/ grid
        row = collections.defaultdict(set)  # Stores a row's visited values
        col = collections.defaultdict(set)  # Stores a col's visited values

        sqr = collections.defaultdict(set)  # Stores a 3 by 3 grid's visited values

        for r in range(9):
            for c in range(9):
                # If the value is not valid integer then we continue
                if board[r][c] == '.':
                    continue
                # If the value is found in the same row before
                # If the value is found in the same col before
                if (board[r][c] in row[r] or
                        board[r][c] in col[c] or
                        board[r][c] in sqr[(r // 3, c // 3)]):  # If the value is found in the same grid before.
                    # [r//3,c//3] provides a particular grid
                    return False
                row[r].add(board[r][c])
                col[c].add(board[r][c])
                sqr[(r // 3, c // 3)].add(board[r][c])

        return True