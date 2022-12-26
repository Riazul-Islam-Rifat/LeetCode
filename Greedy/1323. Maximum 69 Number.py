class Solution:
    def maximum69Number(self, num: int) -> int:

        # Follow official solution

        new_num = num

        current_digit = 0  # Digit count starts from 0th
        first_six = -1

        while new_num:
            if new_num % 10 == 6:
                first_six = current_digit

            new_num //= 10
            current_digit += 1

        if first_six == -1:
            return num
        else:
            return num + 3 * 10 ** first_six
