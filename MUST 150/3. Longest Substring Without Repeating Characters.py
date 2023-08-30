class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Both solutions have a time and space complexity of : O(n)

        # Two pointer approach
        left = 0
        uniqueChar = set()
        length = 0

        for idx, char in enumerate(s):
            while char in uniqueChar:  # Means we have found a character for 2nd or more times
                # When we an counter a char which is repeated, we omit the left most char
                uniqueChar.remove(s[left])
                left += 1
                # At this point we know there is no repeating character
                # So we add the char in the set and calculate the length
            uniqueChar.add(char)
            length = max(length, idx - left + 1)

        return length

        # General approach
        # if s=="":
        #     return 0

        # # Track a character with it's index number
        # lastSeen = {}
        # subString = [0,1] # Initially the first character is the longest one
        # startIdx = 0 # Starting index of the desired subString

        # for idx,val in enumerate(s):
        #     # First we check whether the char is in the lastSeen dict or not
        #     # If it is then we encounter a character for multiple times
        #     # So we don't add it in our subString and we start finding a new subString -->
        #     # after the last occurrence of the val character
        #     if val in lastSeen:
        #         startIdx = max(startIdx, lastSeen[val]+1)

        #     # We check for the largest subString lenght
        #     if subString[1]-subString[0]<idx+1-startIdx:
        #         subString[0] = startIdx
        #         subString[1] = idx+1

        #     # Every time we update the lastSeen of a character
        #     lastSeen[val] = idx

        # return subString[1]-subString[0]