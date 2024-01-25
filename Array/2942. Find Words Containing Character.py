class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:

        output = []

        for word in range(len(words)):
            if x in words[word]:
                output.append(word)

        return output