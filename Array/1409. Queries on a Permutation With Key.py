class Solution:
    def processQueries(self, queries: [int], m: int) -> [int]:
        # Creating the list permutation p with the values 1 to m
        p = [i + 1 for i in range(m)]
        # initializing output list
        output = []

        for count, value in enumerate(queries):
            val_index = p.index(value)  # Finding value's index number from p
            p.pop(val_index)  # pop the value from p
            p.insert(0, value)  # Insert the value at the beginning of p
            output.append(val_index)  # Append the index number in output list

        return output