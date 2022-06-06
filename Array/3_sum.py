def threeSum(nums):
    nums.sort()
    final_array=[]
    if len(nums) < 3:
        return []
    for item, value in enumerate(nums):
        if item>0 and value==nums[item-1]:
            continue
        left_pointer=item+1
        right_pointer=len(nums)-1
        while left_pointer<right_pointer:
            summation=value+nums[left_pointer]+nums[right_pointer]
            if summation>0:
                right_pointer=right_pointer-1
            elif summation<0:
                left_pointer+=1
            else:
                final_array.append([value,nums[left_pointer],nums[right_pointer]])
                left_pointer=left_pointer+1
                while nums[left_pointer]==nums[left_pointer-1] and left_pointer<right_pointer:
                    left_pointer=left_pointer+1
    return final_array

inpt = input()
#target= int(input())
array=list(map(int,inpt.split()))
#print(array)
result=threeSum(array)
print(result)