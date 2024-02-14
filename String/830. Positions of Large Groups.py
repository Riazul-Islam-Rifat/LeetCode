class Solution:
    def largeGroupPositions(self, s: str) -> [[int]]:
        output = []
        c = 1
        start = 0
        for i in range(len(s) - 1):
            if s[i] != s[i + 1] and c >= 3:
                output.append([start, i])
                start = i + 1
                c = 1
            elif s[i] != s[i + 1] and c < 3:
                start = i + 1
                c = 1
            else:
                c += 1
        if c >= 3:
            output.append([start, len(s) - 1])  # Handles the last occurence
        return output



