class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {'A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u'}
        string = list(s)

        l = 0
        r = len(string) - 1

        while l < r:
            while l < r and string[l] not in vowels:
                l += 1
            while l < r and string[r] not in vowels:
                r -= 1
            string[l], string[r] = string[r], string[l]
            l += 1
            r -= 1

        return ''.join(string)

        # Non Optimized

        # vowels = ['A','E','I','O','U','a','e','i','o','u']
        # tracker = []

        # for i in s:
        #     if i in vowels:
        #         tracker.append(i)

        # res = ''
        # j = len(tracker)-1
        # for i in s:
        #     if i in tracker:
        #         res+=tracker[j]
        #         j-=1
        #     else:
        #         res+=i

        # return res