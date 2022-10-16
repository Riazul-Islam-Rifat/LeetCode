class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        mapping = {' ': ' '}
        i = 0
        res = ''
        alphabet = 'abcdefghijklmnopqrstuvwxyz'

        for char in key:
            if char not in mapping:
                mapping[char] = alphabet[i]
                i += 1

        for char in message:
            res += mapping[char]

        return res