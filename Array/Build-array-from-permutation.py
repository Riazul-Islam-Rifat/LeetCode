
def build_array(inpt_list):
    final_list=[]
    for item in range(len(inpt_list)):
        final_list.append(inpt_list[inpt_list[item]])
    return final_list
inpt_list = list(map(int, input().split()))
result=build_array(inpt_list)
print(result)