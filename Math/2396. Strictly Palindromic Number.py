class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:

        # Initializing flag as False
        flag = False

        for item in range(2, n - 1):

            # Converting the integer into Binary
            bin_num = bin(item)[2::]

            # Checking the converted Binary number with it's reverse
            # If the reversed doesn't match then n is not strictly palindromic and false is returned
            # Otherwise flag is set True

            if bin_num != bin_num[::-1]:
                return flag
            else:

                flag = True

        return flag