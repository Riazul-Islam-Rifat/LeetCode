def arr(nums):
    if len(nums) <= 1 or nums==sorted(nums):
        return True
    bool = False
    for item in range(len(nums) - 1):
        if nums[item] <= nums[item + 1]:
            continue
        else:
            var=nums[item]
            nums[item] = nums[item + 1]
            if nums == sorted(nums):
                return True
            else:
                nums[item]=var
                nums[item+1] = nums[item]
                if nums == sorted(nums):
                    return True
                else:
                    break
    return bool



inpt_list = list(map(int, input().split(',')))
result=arr(inpt_list)
print(result)