class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        mod = int(1e9 + 7)

        # Sort lists
        horizontalCuts.sort()
        verticalCuts.sort()

        # We add height and weight to the list
        horizontalCuts.append(h)
        verticalCuts.append(w)

        maxHor = horizontalCuts[0]
        maxVer = verticalCuts[0]

        for i in range(1, len(horizontalCuts)):
            maxHor = max(maxHor, horizontalCuts[i] - horizontalCuts[i - 1])

        for i in range(1, len(verticalCuts)):
            maxVer = max(maxVer, verticalCuts[i] - verticalCuts[i - 1])

        return (maxHor * maxVer) % mod