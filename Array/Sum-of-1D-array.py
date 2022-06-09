def sum(inpt_list):
    nums=inpt_list
    summation=0
    sum_array=[]
    for item in range(len(nums)):
          for i in range(0,item+1):
            summation+=nums[i]
          sum_array.append(summation)
          summation=0
    return sum_array



inpt_list=list(map(int,input().split()))
result=sum(inpt_list)
print(result)