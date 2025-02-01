class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        preSum = 0
        maxAlt = 0

        for i in gain:
            preSum += i
            maxAlt = max(maxAlt, preSum)

        return maxAlt 