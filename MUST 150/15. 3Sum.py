class Solution:
    def threeSum(self, nums: [int]) -> [[int]]:
        # Time complexity: O(N^2)
        # Space complexity: O(N)
        # First sort the input array
        nums.sort()
        triplet = []  # Store the result

        # We will check a possible triplet for each number
        # The last possible triplet might be 3 last elements
        # We will run the loop to the last 3rd element

        for i in range(len(nums) - 2):
            # To avoid iterating an element that is already used
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            # The current sum is the value of the current element
            runningSum = nums[i]
            # Now we will find the rest two elements
            left = i + 1
            right = len(nums) - 1

            while left < right:

                if runningSum + nums[left] + nums[right] == 0:  # Here 0 is the target sum
                    triplet.append([runningSum, nums[left], nums[right]])
                    # When we find a triplet we look for the next one
                    # So we move the pointer
                    left += 1
                    right -= 1
                    # To avoid the duplicate triplets we are moving the right pointer until we reach to a unique value
                    # We can do the same with the left pointer
                    while left < right and nums[right + 1] == nums[right]:
                        right -= 1

                elif runningSum + nums[left] + nums[right] < 0:  # Means we need a larger number
                    left += 1

                else:  # We need a smaller number
                    right -= 1

        return triplet