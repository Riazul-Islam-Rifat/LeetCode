class Solution:
    def sumOddLengthSubarrays(self, arr: [int]) -> int:
        if len(arr) == 1 or len(arr) == 2:
            return sum(arr)

        total = sum(arr)

        for i in range(3, len(arr) + 1, 2):
            c = 0

            for item in range(len(arr) - 2):

                # When we cross the last index, just break the loop
                if i + c > len(arr):
                    break

                total += sum(arr[item:i + c])
                c += 1

        return total