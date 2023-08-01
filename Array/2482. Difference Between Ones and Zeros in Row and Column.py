from itertools import product
class Solution:
    def onesMinusZeros(self, grid: [[int]]) -> [[int]]:
        # col = list(zip(*grid))
        # print(col)
        # row = grid

        # for item in range(len(grid)):

        #     # Calculating number of 1 and 0 for each row
        #     ones_r = grid[item].count(1)
        #     zeros_r = grid[item].count(0)

        #     for i in range(len(col)):

        #         ## Calculating number of 1 and 0 for each column
        #         ones_c = col[i].count(1)
        #         zeros_c = col[i].count(0)

        #         # Updating grid by the given procedure
        #         grid[item][i] = ones_r + ones_c - zeros_r - zeros_c

        # return grid

        R, C = len(grid), len(grid[0])

        rows = list(map(lambda row: 2 * sum(row) - R, grid))
        cols = list(map(lambda col: 2 * sum(col) - C, zip(*grid)))
        print(rows)
        print(cols)
        for i, j in product(range(R), range(C)): # For using product we get i,j like 0,0-0,1-0,2-1,0-1,1 ......
            grid[i][j] = rows[i] + cols[j]

        return grid