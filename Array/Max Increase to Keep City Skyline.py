class Solution:
    def maxIncreaseKeepingSkyline(self, grid) -> int:
        row_max = [max(row) for row in grid]
        col_max = [max(col) for col in zip(*grid)]
        summ = 0
        for row, val in enumerate(grid):
            for count, height in enumerate(val):
                summ += min(row_max[row], col_max[count]) - height

        return summ