class Solution:
    def productExceptSelf(self, nums: [int]) -> [int]:
        # Find the left product of an index excluding that index
        leftProduct = [1]*len(nums)
        for i in range(1,len(nums)):
            leftProduct[i] = leftProduct[i-1]*nums[i-1]
        print(leftProduct)
        # Find the right product of an index excluding that index
        rightProduct = [1]*len(nums)
        for i in range(len(nums)-2,-1,-1):
            rightProduct[i] = rightProduct[i+1]*nums[i+1]
        print(rightProduct)

        # Now multiply leftProduct and rightProduct to get the answer
        ans = []

        for i in range(len(nums)):
            ans.append(leftProduct[i]*rightProduct[i])

        return ans

        # Time complexity: O(N)
        # Space complexity: O(N)


        # With Space complexity of O(1)
        # Find the left product of an index excluding that index
        ans = [1]*len(nums)
        for i in range(1,len(nums)):
            ans[i] = ans[i-1]*nums[i-1]
        print(ans)
        # Find the right product of an index excluding that index
        rightProduct = 1
        for i in range(len(nums)-2,-1,-1):
            rightProduct = rightProduct*nums[i+1]
            ans[i] = ans[i]*rightProduct # Update the answer

        return ans
