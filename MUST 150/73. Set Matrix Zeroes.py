class Solution:
    def setZeroes(self, matrix: [[int]]) -> None:
        # Time complexity: O(n*m)
        row = len(matrix)
        col = len(matrix[0])
        rowZero = False
        # We will use the first row and column to track which row/column should be 0
        for r in range(row):
            for c in range(col):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0  # Makes the column 0
                    if r > 0:
                        matrix[r][0] = 0  # Makes the row 0
                    else:
                        rowZero = True  # To track whether the first row/col should be 0 or not

        for r in range(1, row):
            for c in range(1, col):
                if matrix[0][c] == 0 or matrix[r][0] == 0:  # If the row / col needs to be 0 then assign value 0
                    matrix[r][c] = 0

        if matrix[0][0] == 0:  # Assign 0 to the first row
            for r in range(row):
                matrix[r][0] = 0

        if rowZero:
            for c in range(col):  # Assign 0 to the first col
                matrix[0][c] = 0