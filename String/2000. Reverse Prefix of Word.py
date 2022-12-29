class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch not in word:
            return word

        # Find the index of the given character
        index = word.index(ch)

        # Retrieve the prefix from word
        prefix = word[:index + 1]
        # Reverse the prefix
        prefix = prefix[::-1]

        # Separate the suffix from word
        suffix = word[index + 1:len(word)]

        # Add prefix and suffix and then return
        return prefix + suffix