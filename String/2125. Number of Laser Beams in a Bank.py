class Solution:
    def numberOfBeams(self, bank: [str]) -> int:
        # initializing summ and prev_cell
        summ = 0
        prev_cell = 0

        for item in range(len(bank) - 1):
            current_cell = bank[item].count("1")  # Finding number of 1s in current row
            next_cell = bank[item + 1].count("1")  # Finding number of 1s in the next row

            # If number of 1s in current row and next row is 0 then we move to the next iteration
            if next_cell == 0 and current_cell == 0:
                pass

            # If number of 1s in next_cell is 0 then we store the number of 1s of the current row in prev_cell
            elif next_cell == 0 and current_cell != 0:
                prev_cell = current_cell

            else:
                # prev_cell will hold non-zero value when there exists row(s) in between two rows without security device
                if prev_cell != 0:
                    summ += (prev_cell * next_cell)
                    prev_cell = 0  # To update the value of prev_cell in next iterations

                # prev_cell will hold zero value when there doesn't exist row(s) in between two rows without security device
                else:
                    summ += (current_cell * next_cell)

        return summ
