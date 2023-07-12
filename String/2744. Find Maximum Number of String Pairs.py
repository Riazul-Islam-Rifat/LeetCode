class Solution:
    def maximumNumberOfStringPairs(self, words: [str]) -> int:

        wordSet = set(words)
        count = 0
        for item in words:
            word = item[::-1]  # Reverse the word
            wordSet.remove(item)  # It works for test cases like ['ba','ab','aa']--> Doesn'r count aa
            if word in wordSet:
                words.remove(word)  # To avoid double count and to satisfy i < j condition.
                count += 1

        return count

        # Time complexity : O(N)
        # Space complexity : O(1)