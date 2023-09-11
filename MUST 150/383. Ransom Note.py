class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # Time and space complexity: O(n)
        ranSomDict = dict(Counter(ransomNote))
        magDict = dict(Counter(magazine))

        for key in ranSomDict:
            if key not in magazine or ranSomDict[key] > magDict[key]:
                return False

        return True