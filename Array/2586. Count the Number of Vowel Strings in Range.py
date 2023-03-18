class Solution:
    def vowelStrings(self, words: [str], left: int, right: int) -> int:
        vowel_set = {'a','e','i','o','u'}
        vowel_string = 0

        for item in range(left,right+1):
            if words[item][0] in vowel_set and words[item][-1] in vowel_set:
                vowel_string+=1

            else:
                continue

        return vowel_string