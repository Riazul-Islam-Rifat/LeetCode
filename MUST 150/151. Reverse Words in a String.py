class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()  # Remove starting and trailing spaces
        words = []
        startOfWord = 0
        i = 0
        # Store s with a single space in between words
        while i < (len(s)):
            if s[i] == " " and s[startOfWord] != " ":  # Means we got a new word
                words.append(s[startOfWord:i])  # We append the word
                startOfWord = i  # Take a space to add in between words
                i += 1
            elif s[i] != " " and s[startOfWord] == " ":
                # We will add a single space in between words
                words.append(s[startOfWord])
                startOfWord = i
                i += 1
            # Ignore multiple space
            else:
                i += 1

        # Add the last word
        words.append(s[startOfWord:len(s)])
        # Now we have the sentence with a single space in between words
        # Reverse the words list
        start = 0
        end = len(words) - 1
        while start < end:
            words[start], words[end] = words[end], words[start]
            start += 1
            end -= 1

        # Now return the list in string
        return ''.join(words)

        # Time complexity: O(n)
        # Space complexity: O(n)