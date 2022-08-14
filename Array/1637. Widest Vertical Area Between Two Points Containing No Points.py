class Solution:
    def maxWidthOfVerticalArea(self, points) -> int:
        x_points=list(zip(*points))
        x_axis=list(x_points[0])
        x_axis.sort()
        max_width=0
        for item in range(0,len(x_axis)-1):
            max_width=max((abs(x_axis[item]-x_axis[item+1])),max_width)
        return max_width