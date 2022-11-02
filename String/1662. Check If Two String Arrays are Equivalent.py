from typing import List

class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:

        string1 = ''
        string2 = ''

        # Creating string1 with the items of word1
        for item in word1:
            string1 += item
        # Creating string2 with the items of word2
        for item in word2:
            string2 += item

        # Comparing String1 and String2
        return True if string1 == string2 else False