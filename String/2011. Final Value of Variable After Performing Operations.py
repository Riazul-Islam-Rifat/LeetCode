class Solution:
    def finalValueAfterOperations(self, operations) -> int:
        x = 0
        for item in operations:
            if item == "--X":
                x -= 1
            elif item == "X--":
                x -= 1

            elif item == '++X':
                x += 1

            elif item == "X++":
                x += 1

        return x