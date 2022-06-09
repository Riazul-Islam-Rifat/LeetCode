
def concatenation(inpt_list):
    nums=inpt_list
    final_list=[]
    final_list.extend(nums)
    final_list.extend(nums)
    return final_list

inpt_list=list(map(int,input().split()))
result=concatenation(inpt_list)
print(result)