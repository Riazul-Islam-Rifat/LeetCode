class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # Time complexity: O(N)--> O(n*n)
        left = 0
        right = len(matrix)-1

        while left < right:
            top = left
            bottom  = right

            for i in range(right-left): # [l=0, r=3 so range(0-2)]
                # Store the top left value
                TopLeft = matrix[top][left+i]

                # Move left bottom to top left
                matrix[top][left+i] = matrix[bottom-i][left]

                # Move bottom right to the bottom left
                matrix[bottom-i][left] = matrix[bottom] [right-i]

                # Move top right to the bottom right
                matrix[bottom][right-i] = matrix[top+i][right]

                matrix[top+i][right] =  TopLeft

            left+=1
            right-=1
        return matrix
