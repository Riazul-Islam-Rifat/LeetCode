# Best case solution
def step(nums):
    n = len(nums)

    dp = [0]*n
    stack = []

    for i in range(n - 1, -1, -1):
        while stack and nums[i] > nums[stack[-1]]:
            dp[i] = max(dp[i] + 1, dp[stack.pop()])
        stack.append(i)

    return max(dp)


inpt_list = list(map(int, input().split(',')))
result=step(inpt_list)
print(result)


# Worst case solution


'''def step(nums):
    steps=0

    length=len(nums)
    while nums!=sorted(nums):
        track_array = []
        for item in range(1,len(nums)):
            if nums[item-1]>nums[item]:
                track_array.append(item)
        for count,item in enumerate(track_array):
            if count==0:
                del(nums[item])
            else:
                del(nums[item-count])
        steps+=1

    return steps

    # if nums!=sorted(nums):
    #     steps+=1
    #     step(nums)
    # else:
    #     return steps
inpt_list = list(map(int, input().split(',')))
result=step(inpt_list)
print(result)'''
