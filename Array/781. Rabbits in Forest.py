from collections import Counter
import math


class Solution:
    def numRabbits(self, answers: [int]) -> int:
        tracker = Counter(answers)
        rabbits = 0
        for key, value in tracker.items():
            rabbits += ((key + 1) * (math.ceil(value / (key + 1))))
        return rabbits

