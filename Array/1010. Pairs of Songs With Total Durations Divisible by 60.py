class Solution:
    def numPairsDivisibleBy60(self, time: [int]) -> int:
        # Time complexity -- O(n^2)
        # counter = 0
        # for i in range(len(time)):
        #     for j  in  range(i+1,len(time)):
        #         if (time[i]+time[j])%60==0:
        #             counter+=1

        # return  counter

        # Time complexity: O(N)
        res = 0
        tracker = [0]*60 #  As we are working for divisible by 60

        for num in time:
            remainder = num%60
            res += tracker[60-remainder] if remainder>0 else tracker[0]
            tracker[remainder]+=1

        return res