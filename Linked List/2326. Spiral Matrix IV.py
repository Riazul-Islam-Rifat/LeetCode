# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import numpy as np


class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        output = np.full((m, n), -1)
        sRow = 0
        sCol = 0
        eRow = m - 1
        eCol = n - 1

        while sRow <= eRow and sCol <= eCol:
            # from left to right
            for col in range(sCol, eCol + 1):
                if head:
                    output[sRow][col] = head.val
                    head = head.next

            # from top tp bottom
            for row in range(sRow + 1, eRow + 1):
                if head:
                    output[row][eCol] = head.val
                    head = head.next

            # from right to left
            for col in range(eCol - 1, sCol - 1, -1):
                if sRow == eRow:  # To handle the single row
                    break
                if head:
                    output[eRow][col] = head.val
                    head = head.next

            # from bottom to top
            for row in range(eRow - 1, sRow, -1):
                if sCol == eCol:  # When there is a single column
                    break
                if head:
                    output[row][sCol] = head.val
                    head = head.next

            sRow += 1
            sCol += 1
            eRow -= 1
            eCol -= 1

        return output