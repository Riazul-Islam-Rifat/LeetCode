class Solution:
    def partitionLabels(self, s: str) -> [int]:
        # storing last occurence index number of each character in a dictionary.
        # dictionary key--> character, value--> character's index number
        # value is updated in each iteration for repeated character
        last_occurence = {ch: i for i, ch in enumerate(s)}

        # Initializing two variables
        start = end = 0
        # initializing the output list
        output = []

        for index, ch in enumerate(s):
            # for each character we compare it's last occurence index number with current end
            # end becomes max of current end and character's last occurence index number
            end = max(end, last_occurence[ch])

            if end == index:
                # when end is same as index then partition occurs
                # Next append the partition's length in output list
                output.append(index - start + 1)
                start = index + 1

        return output