class Solution:
    def maxDepth(self, s: str) -> int:

        # Initializing ans variable to store the max nesting depth
        ans = 0
        # Using stack to store "("
        stack = []

        # Iterate the given string
        for item in s:
            if item == "(":
                stack.append(item)
                ans = max(ans, len(stack))

            elif item == ")":
                stack.pop()

        return ans