class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # Time complexity: O(N)
        if numRows == 1:
            return s
        result = ''
        for row in range(numRows):
            increment = (numRows-1) * 2
            for i in range(row,len(s),increment):
                # Works for the first and last row
                result+=s[i]
                # Works for the middle row [For the V shaped characters]
                if row>0 and row<numRows-1 and i+increment - 2*row<len(s):
                    result+=s[i+increment - 2*row]

        return result
