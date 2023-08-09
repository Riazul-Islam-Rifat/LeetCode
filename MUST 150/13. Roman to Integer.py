class Solution:
    def romanToInt(self, s: str) -> int:
        # Store the roman value in a hash table
        roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        result = 0
        for i in range(len(s)):
            # Make sure index is not out of bound
            # When the left digit is smaller than right digit we subtract the left number
            if i+1<len(s) and roman[s[i]]<roman[s[i+1]]:
                result-=roman[s[i]]

            else:
                result+=roman[s[i]]

        return result

    # Time complexity: O(n)
    # Space complexity: O(1) as the dictionary is fixed with 7 elements.