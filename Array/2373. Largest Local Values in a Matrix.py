class Solution:
    def largestLocal(self, grid: [[int]]) -> [[int]]:

        output = []

        for i in range(len(grid) - 2):
            row = []

            for j in range(len(grid) - 2):
                k = []
                k.append(grid[i][j])
                k.append(grid[i][j + 1])
                k.append(grid[i][j + 2])
                k.append(grid[i + 1][j])
                k.append(grid[i + 1][j + 1])
                k.append(grid[i + 1][j + 2])
                k.append(grid[i + 2][j])
                k.append(grid[i + 2][j + 1])
                k.append(grid[i + 2][j + 2])
                m = max(k)
                row.append(m)

            output.append(row)

        return output