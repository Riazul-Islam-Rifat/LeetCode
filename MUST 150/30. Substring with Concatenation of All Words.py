class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        # Time complexity: O(N * len(subStr))

        wordDict = dict(Counter(words))  # Represents number of each word in the list
        subStringLength = len(words) * len(words[0])
        wordLength = len(words[0])
        res = []
        i = 0

        while i < len(s) - subStringLength + 1:
            # Take a substring
            subStr = s[i:i + subStringLength]
            tracker = {}
            j = 0
            # Work on that sub string
            while j < len(subStr) - wordLength + 1:
                # Take each word of that substring
                word = subStr[j:j + wordLength]
                # Update the tracker dictionary
                if word in tracker:
                    tracker[word] += 1
                else:
                    tracker[word] = 1
                # Amount of each word in tracker should be less or equal to the wordDict's one.
                if word in wordDict and tracker[word] <= wordDict[word]:
                    if j == len(subStr) - wordLength:
                        res.append(i)
                else:
                    break

                j += wordLength  # Update j for the next word

            i += 1  # Update i for the next subString
        return res