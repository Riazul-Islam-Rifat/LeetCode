import numpy as np


class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        mat = np.zeros((n, n), dtype=np.int16)

        for item in queries:
            row1, col1, row2, col2 = item
            mat[row1:row2 + 1, col1:col2 + 1] += 1

        return mat