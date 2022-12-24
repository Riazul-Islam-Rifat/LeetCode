class Solution:
    def balancedStringSplit(self, s: str) -> int:

        output = 0
        counter = 0

        for item in s:
            if item == 'R':
                counter+=1

            elif item == 'L':
                counter-=1

            if counter==0:
                output+=1

        return output