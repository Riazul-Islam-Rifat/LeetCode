class Solution:
    def checkIfPangram(self, sentence: str) -> bool:

        # Initializing an empty string to store unique characters of the sentence
        alphabet = ''

        for item in sentence:
            if item not in alphabet:
                alphabet += item

        return True if len(alphabet) == 26 else False

        # Solution 2
        # return True if len(set(sentence))== 26 else False