class Solution:
    def leftRigthDifference(self, nums: [int]) -> [int]:
        answer = [0 for item in range(len(nums))]
        leftSum = [0]*len(nums)
        rightSum = [0]*len(nums)

        CurleftSum = 0
        for item in range(1,len(answer),1):
            CurleftSum+=nums[item-1]
            leftSum[item] = CurleftSum

        CurRightSum = 0
        for item in range(len(nums)-2,-1,-1):
            CurRightSum+=nums[item+1]
            rightSum[item] = CurRightSum

        for item in range(len(answer)):
            answer[item]=abs(leftSum[item]-rightSum[item])

        return answer