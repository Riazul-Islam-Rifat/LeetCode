from typing import List
from collections import Counter
class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        arr1 = Counter(
            words1)  # arr1 is a dictionary where keys are the word and values are the number of appearance  of that word
        arr2 = Counter(words2)

        counter = 0  # To track the desired number of strings

        for key in arr1.keys():
            # When a word appears only once in each dictionary then counter ++
            if key in arr2.keys() and arr1[key] == arr2[key] == 1:
                counter += 1

        return counter