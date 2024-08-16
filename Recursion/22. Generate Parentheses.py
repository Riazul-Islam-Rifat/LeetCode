class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # As long as open < n we can add (
        # If close < open we can add )
        # If opne == close == n (number of paranthesis) then we will find a valid form.

        stack = []
        res = []

        def backtrack(open, close):
            if open == close == n:
                res.append("".join(stack))

            if open < n:
                stack.append('(')
                backtrack(open+1, close)
                stack.pop() # We pop a parenthesis when it's role is done as we are maintaining a single stack

            if close < open:
                stack.append(')')
                backtrack(open, close+1)
                stack.pop()
        backtrack(0,0)
        return res