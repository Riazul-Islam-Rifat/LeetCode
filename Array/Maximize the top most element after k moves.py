import random
def maximize(nums,k):
    if len(nums)==0:
        return -1
    if len(nums)==1:
        if k%2==0:
            return nums[0]
        else:
            return -1
    if k==1:
        return nums[1]
    if k==0:
        return nums[0]
    if k>len(nums):
        return max(nums)
    if k == len(nums):
        return max(nums[:k-1])
    if k>1 and k <len(nums):
            return max(max(nums[:k-1]),nums[k])


inpt_list=list(map(int,input().split(',')))
k=int(input())
result=maximize(inpt_list,k)
print(result)