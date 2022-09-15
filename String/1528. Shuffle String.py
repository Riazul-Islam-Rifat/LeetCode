from typing import List
class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:

        # creating a list named shuffle with a same length of s
        shuffle = [0 ] *len(s)

        # In zip() function s & indices are passed
        # z looks like [('c', 4), ('o', 5), ('d', 6), ('e', 7), ('l', 0), ('e', 2), ('e', 1), ('t', 3)]

        z= list(zip(s,indices))

        for item in z:
            # Updating each index of shuffle with desired character
            shuffle[item[1]]=item[0]

        # list to string
        shuffle= "".join (shuffle)
        return shuffle