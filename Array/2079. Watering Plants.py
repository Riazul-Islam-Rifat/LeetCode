from typing import List

class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:

        # Initializing steps and storing capacity in c
        steps = 0
        c = capacity

        for index, value in enumerate(plants):
            if value <= c:
                steps += 1
                c = c - value

            else:
                steps = steps + index + index + 1
                c = capacity - value

        return steps