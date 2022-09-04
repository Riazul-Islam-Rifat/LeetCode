from collections import defaultdict
from typing import  List
class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:

        pattern_map = defaultdict(list)
        for index, value in enumerate(pattern):
            pattern_map[value].append(index)

        pattern_map_value = []
        output = []

        for item in pattern_map.values():
            pattern_map_value.append(item)

        for index, value in enumerate(words):
            value_map = defaultdict(list)
            value_map_val = []

            for count, val in enumerate(value):
                value_map[val].append(count)

            if len(value_map) == len(pattern_map):

                for item in value_map.values():
                    value_map_val.append(item)

                if value_map_val == pattern_map_value:
                    output.append(value)

        return output