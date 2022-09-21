class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        # Split the given input string and store in list_of_string
        list_of_string = s.split(" ")

        # Initialize output_str
        output_str = ""

        for item in range(k):
            # Concatenate items of list_of_string to generate the desired output
            output_str = output_str + " " + list_of_string[item]

            # Discard the first space and return the desired output
        return output_str[1::]