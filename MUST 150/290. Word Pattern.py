class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
      # Time and space complexity: O(n)
      patDict = defaultdict(list)
      sDict = defaultdict(list)
      sList = s.split(' ')
      if len(sList)!=len(pattern):
        return False
      for item in range(len(sList)):
        patDict[pattern[item]].append(item)
        sDict[sList[item]].append(item)

      return list(patDict.values())==list(sDict.values())