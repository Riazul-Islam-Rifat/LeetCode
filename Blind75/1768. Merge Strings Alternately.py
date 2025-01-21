class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        print(len(word1))
        pointer = 0
        res = ''
        while pointer < len(word1) and pointer <len(word2):

            res+=word1[pointer]
            res+=word2[pointer]
            pointer+=1

        res+=word1[pointer:len(word1)]
        res+=word2[pointer:len(word2)]

        return res