class Solution:
    def candy(self, ratings: [int]) -> int:
        # Time complexity: O(n)
        # Space complexity: O(n)

        minCandy = [1]*len(ratings)
        print(minCandy)
        # Left to right --> works for 1,2,3---
        for i in range(1,len(ratings)):
            if ratings[i]>ratings[i-1]: # When the right neighbor is greater
                minCandy[i] = minCandy[i-1]+1
        # Right to left--> Works for 3,2,1---
        for i in reversed(range(len(ratings)-1)):
            if ratings[i]>ratings[i+1]:
                minCandy[i] = max(minCandy[i],minCandy[i+1]+1)
        return sum(minCandy)