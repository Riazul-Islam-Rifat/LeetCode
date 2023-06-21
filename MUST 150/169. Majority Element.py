class Solution:
    def majorityElement(self, nums: List[int]) -> int:
    # Boyer - Moore algorithm
    # With time complexity o(n).
        result = 0
        count = 0

        for num in nums:
            # When count is 0 then the num is assigned to the result
            if count == 0:
                result = num

            if num == result:
                count+=1
            else:
                count-=1

        return result




# As the majority element appears more than [n/2] times hence that element will be [n//2]th element after sorting
        nums.sort()
        return nums[len(nums)//2]

# Time complexity O(nlogn)