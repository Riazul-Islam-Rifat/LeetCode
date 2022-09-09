from typing import  List
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:

        # separating all x values and y values

        x_part =nums[0:n] # storing all x values (x1 x2 x3 ...) in x_part
        y_part= nums[n::] # storing all y values (y1 y2 y3 ....) in y_part

        # initializing output list

        output =[]

        for item in range(n):

            # Append in x1y1 x2y2  .... XnYn manner
            output.append(x_part[item])
            output.append(y_part[item])


        return output