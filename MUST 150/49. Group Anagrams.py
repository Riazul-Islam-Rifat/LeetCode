from collections import  defaultdict
class Solution:
    def groupAnagrams(self, strs: [str]) -> [[str]]:
        # Time complexity : O(n*m)
        res = defaultdict(list)

        for s in strs:
            count = [0] * 26  # Makes a list like [0,0,0,......,0,0]

            for c in s:
                count[ord(c) - ord('a')] += 1  # [ord(c)-ord('a')] Find the corresponding index of c
            # count list will be the same  for the words those are anagram to each other
            res[tuple(count)].append(s)  # List can't be a key so we make it tuple

        return res.values()