import string


class Solution:
    def uniqueMorseRepresentations(self, words: [str]) -> int:

        signs = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.",
                 "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]

        letters = string.ascii_lowercase

        # Initializing tracker list to store unique transformation
        tracker = []

        for item in words:
            transformation = ''

            for i in item:
                transformation += signs[letters.index(i)]

            if transformation not in tracker:
                tracker.append(transformation)

        return len(tracker)

