from typing import List
from collections import defaultdict
class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        column = len(mat[0])
        row = len(mat)

        # Initializing default dictionary object . Value type LIST
        diagonal_dict = defaultdict(list)

        # Storing the diagonal values.
        # Here automate keys are generated (as defaultdict) and values are appended to those keys
        for i in range(row):
            for j in range(column):
                diagonal_dict[i - j].append(mat[i][j])

        # Sorting the diagonal values
        for k in diagonal_dict:
            diagonal_dict[k].sort()

        # Updating diagonal values with the sorted values
        for i in range(row):
            for j in range(column):
                mat[i][j] = diagonal_dict[i - j].pop(0)

        # Returning the updated mat
        return mat