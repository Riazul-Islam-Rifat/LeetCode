class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        res = []

        for i in nums:
            if nums.count(i)>1:
                if i not in res:
                    res.append(i)

        return res