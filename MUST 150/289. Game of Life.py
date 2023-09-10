class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        # Time complexity: O(N)
        # We will assign values [0/1/2/3] according to it's new state
        # 0 -- > 0 == 0
        # 1 -- > 0 == 1
        # 0 -- > 1 == 2
        # 1 -- > 1 == 3

        def getNeighbor(r, c):
            nei = 0
            for i in range(r - 1, r + 2):
                for j in range(c - 1, c + 2):
                    if ((i == r and j == c) or i < 0 or j < 0 or i == len(board) or j == len(board[0])):
                        # When out of bounds
                        continue
                    if board[i][j] in [1, 3]:
                        nei += 1

            return nei

        for r in range(len(board)):
            for c in range(len(board[0])):
                neiOnes = getNeighbor(r, c)  # Takes the number of ones of it's neighbors
                if board[r][c] == 1:
                    if neiOnes in [2, 3]:  # neiOnes is 2 or 3
                        board[r][c] = 3  # Means it's old state is 1 and new is also 1.
                    # We skip the else part as 1 stays 1.
                    # else:
                    #     board[r][c] = 1 # Means it's old state is 1 and new is 0.

                else:  # When board[r][c] ==0
                    if neiOnes == 3:
                        board[r][c] = 2  # Means it's old state is 0 and new is 1.
                    # We skip the else part when 0 stays 0.

        # Re-assign the values 0 and 1 again
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == 1:  # When new state is 0
                    board[r][c] = 0
                elif board[r][c] in [2, 3]:  # When new state is 1
                    board[r][c] = 1
