class Solution:
    def countConsistentStrings(self, allowed: str, words: [str]) -> int:

        l = len(words)

        for item in words:

            flag = True

            for i in item:
                if i not in allowed:
                    flag = False
                    break

            if not flag:
                l -= 1

        return l