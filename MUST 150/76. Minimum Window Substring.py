class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Base case
        if t == '': return ''

        # Number of each character in t
        countT = {}
        for char in t:
            countT[char] = 1 + countT.get(char, 0)  # Initially takes 0 and then add the char

        # need character and have character
        have, need = 0, len(countT)  # Initially we have 0 characters but we need all unique characters
        left = 0
        right = 0
        # We will take each char and make a substr where all t's chars exist.
        # Then we will omit from left and check whether it is still valid or not.

        # window to store running substr
        window = {}
        res = [-1, -1]
        resLen = float('inf')
        while right < len(s):
            char = s[right]
            window[char] = 1 + window.get(char, 0)  # Update the substr window

            if char in countT and window[char] == countT[char]:
                # Means we have found a char exactly how many we need for our substr
                # So we have a character now
                have += 1

            # When have and need are same we will omit from left and minimize the len of substr if possible
            while have == need:
                # Means we have found a desired substr so we update our result if the current substr is smaller
                if right + 1 - left < resLen:
                    res = [left, right + 1]
                    resLen = right + 1 - left

                leftChar = s[left]
                window[leftChar] -= 1  # We omit the left char

                # After omitting  leftChar if window contains that char less than t contains
                # means we have lost a needed char so we have less now
                if leftChar in countT and window[leftChar] < countT[leftChar]:
                    have -= 1
                left += 1
            right += 1

        return s[res[0]:res[1]] if resLen != float('inf') else ''
