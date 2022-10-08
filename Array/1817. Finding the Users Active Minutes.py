from collections import defaultdict
from typing import List


class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        # Initializing a dictionary to store each user's active minutes
        unique_AM = defaultdict(list)

        for item in logs:
            if item[1] not in unique_AM[item[0]]:
                unique_AM[item[0]].append(item[1])

        # Initializing a list with the length of K
        UAM = [0] * k

        # Overall user's 
        unique_min = []

        for item in unique_AM.values():
            unique_min.append(len(item))

        for item in unique_min:
            UAM[item - 1] += 1

        return UAM