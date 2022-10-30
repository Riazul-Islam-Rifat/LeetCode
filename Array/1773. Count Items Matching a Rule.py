from typing import List
class Solution:
    def countMatches(self, items: [List[str]], ruleKey: str, ruleValue: str) -> int:
        # Initializing a variable to store  number of items that match the given rule
        matched_item = 0
        for item in items:
            # Checking type with the given in ruleValue
            if ruleKey == "type":
                if item[0] == ruleValue:
                    matched_item += 1

            # Checking color with the given color in ruleValue
            elif ruleKey == "color":
                if item[1] == ruleValue:
                    matched_item += 1

            # Checking name with the given name in ruleValue
            elif ruleKey == "name":
                if item[2] == ruleValue:
                    matched_item += 1

        return matched_item