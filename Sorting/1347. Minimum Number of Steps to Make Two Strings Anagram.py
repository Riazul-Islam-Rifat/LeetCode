class Solution:
    def minSteps(self, s: str, t: str) -> int:

        # Initializing the steps variable and frequency_dict dictionary
        steps = 0
        frequency_dict = {}

        # Initializing traversed variable
        traversed = ""

        for item in range(len(s)):
            # Storing frequencies of each character

            if s[item] in t:
                if s[item] not in frequency_dict.keys():
                    frequency_dict[s[item]] = s.count(s[item])

            # When a character of s is absent in t, we add the frequency of that character with steps
            else:
                if s[item] not in traversed:
                    steps += s.count(s[item])
                    traversed += s[item]

        for item in range(len(t)):
            # Finding the frequencies of each character of t then
            # finding the frequency difference of a same character of s and t
            # add the difference with the value of steps

            if t[item] in frequency_dict.keys() and t[item] not in traversed:
                if (frequency_dict.get(t[item]) - t.count(t[item])) > 0:
                    steps += (frequency_dict.get(t[item]) - t.count(t[item]))

            traversed += t[item]

        return steps

