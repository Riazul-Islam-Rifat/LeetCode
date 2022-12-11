class Solution:
    def prefixCount(self, words: [str], pref: str) -> int:

        # Initializing a variable named count
        count = 0
        for item in words:
            # Checking whether the pref exists as a leading substring
            if item[0:len(pref)] == pref:
                count += 1

        return count