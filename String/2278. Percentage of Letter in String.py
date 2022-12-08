class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:

        # If letter doesn't even exist then percentage is 0.
        if letter not in s:
            return 0

        else:  # Calculate and return the percentage
            return int(s.count(letter) / len(s) * 100)