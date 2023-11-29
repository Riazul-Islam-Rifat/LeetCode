class Solution:
    def findMinArrowShots(self, points: [[int]]) -> int:
        # Sort the points
        sortedPoints = sorted(points,key = lambda interval:interval[1])
        print(sortedPoints)
        left = 0
        right = 1
        shoot = 0
        while left< len(sortedPoints) and right<len(sortedPoints):
            endTime = sortedPoints[left][1]
            startTime = sortedPoints[right][0]
            if endTime<startTime:
                shoot+=1
                left = right
            right+=1
        print(shoot)
        return shoot+1 # For the last interval we add one


# Time complexity -- O(n log n)