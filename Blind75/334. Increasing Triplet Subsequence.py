class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        min1 = float('inf')  # First number (smallest one)
        min2 = float('inf')  # Second number (middle one)

        for num in nums:
            # print(min1,min2)
            if num <= min1:
                min1 = num  # Found the smallest number
            elif num <= min2:
                min2 = num  # Found the second number

            else:
                return True  # Found the triplet
        # print(min1,min2)
        return False