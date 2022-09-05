class Solution:
    def rearrangeArray(self, nums: [int]) -> [int]:

        # Initializinf the output list
        output = []

        # Initializing two different lists to store positive and negative numbers separately number.
        pos_num = []
        neg_num = []

        for item in nums:
            if item > 0:
                pos_num.append(item)  # storing positive numbers in pos_num

            else:
                neg_num.append(item)  # storing negative numbers in neg_num

        for item in range(len(pos_num)):  # len(neg_num) is same as len(pos_num)

            # First appending a positive number then a negative number in each iteration
            output.append(pos_num[item])
            output.append(neg_num[item])

        return output