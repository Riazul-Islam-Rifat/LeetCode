class Solution:
    def isValid(self, s: str) -> bool:
        # Time and space complexity: O(n)
        openingBracs = '({['
        closingBracs = ')}]'
        matchingPairs = {')': '(', '}': '{', ']': '['}
        stack = []
        for i in s:
            if i in openingBracs:
                stack.append(i)
            elif i in closingBracs:
                if len(stack) == 0 or stack[-1] != matchingPairs[i]:  # if i is ] then stack[-1] must be [
                    return False
                else:
                    stack.pop()  # When [ matches with ] then pop out [ from stack

        return len(stack) == 0
