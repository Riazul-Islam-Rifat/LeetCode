class Solution:
    def firstPalindrome(self, words: [str]) -> str:
        for item in words:
            reversed_item = ''.join(reversed(item))
            if item==reversed_item:
                return item

        return ''