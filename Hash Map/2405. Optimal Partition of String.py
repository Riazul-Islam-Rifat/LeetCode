class Solution:
    def partitionString(self, s: str) -> int:
        count = 0
        string = ''
        for item in s:
            # When there will be more than one same character in the string then the if condition will be executed
            if item in string:
                count+=1
                string =''

            string+=item
        # Adding 1 as the last item won't satisfy the if condition but it itself an unique substring
        return count+1