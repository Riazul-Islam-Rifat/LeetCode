import string
from typing import List

class Solution:
    def oddString(self, words: List[str]) -> str:
        alphabet = string.ascii_lowercase
        difference_int_arr = []
        tracker = []
        for count, val in enumerate(words):
            d_i_r = []
            for item in range(len(val) - 1):
                d_i_r.append(alphabet.index(words[count][item + 1]) - alphabet.index(words[count][item]))

            difference_int_arr.append(d_i_r)
            tracker.append(val)

        for item in difference_int_arr:
            if difference_int_arr.count(item) == 1:
                return tracker[difference_int_arr.index(item)]