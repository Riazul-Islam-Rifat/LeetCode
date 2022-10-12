class Solution:
    def minimumSum(self, num: int) -> int:
        # Converting the num into string
        num = str(num)

        # Storing each digits as an element in a list
        num_list = []
        for item in num:
            num_list.append(int(item))

        num_list.sort()

        # Forming num1 and num2 from the sorted list [num_list]
        num1 = int(str(num_list[0]) + str(num_list[2]))
        num2 = int(str(num_list[1]) + str(num_list[3]))

        # returning the minimum sum

        return num1 + num2