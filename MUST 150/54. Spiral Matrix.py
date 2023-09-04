class Solution:
    def spiralOrder(self, matrix: [[int]]) -> [int]:
        # Time complexity: O(matrixSize) as each elemetn is traversed for once

        ans = []  # To store the answer

        sRow = 0  # Starting row
        sCol = 0  # Strating colum
        eRow = len(matrix) - 1  # Ending row
        eCol = len(matrix[0]) - 1  # Ending colum

        while sRow <= eRow and sCol <= eCol:
            # Left to Right
            for i in range(sCol, eCol + 1):  # Each element in a colum
                ans.append(matrix[sRow][i])

            # Top to bottom
            for i in range(sRow + 1, eRow + 1):  # Top to bottom row elements
                ans.append(matrix[i][eCol])

            # Right to left
            for i in range(eCol - 1, sCol - 1, -1):
                # This condition handles the situation when there will be a single row
                if sRow == eRow:
                    break
                ans.append(matrix[eRow][i])

            # Bottom to top
            for i in range(eRow - 1, sRow, -1):
                # This condition handles the sutitation when there will be a single col
                if sCol == eCol:
                    break
                ans.append(matrix[i][sCol])

            sRow += 1
            sCol += 1
            eRow -= 1
            eCol -= 1
        return ans