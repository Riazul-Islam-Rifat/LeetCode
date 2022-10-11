from typing import List

class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        # Initializing the output list with the first element of pref to store the values of prefix xor
        output = [pref[0]]

        if len(pref) == 1:
            return output

        for item in range(len(pref) - 1):
            # Finding the xor value of two consecutive elements of pref
            output.append((pref[item] ^ pref[item + 1]))

        return output