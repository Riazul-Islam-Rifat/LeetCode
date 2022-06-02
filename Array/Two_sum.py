given_arr=input()
modified_arr=str(given_arr[1:-1])
array=list(map(int, modified_arr.split(',')))
target_num=int(input())
#final_arr=[]
final_arr=''
for item in range(0,len(array)):
    for i in range(item+1,len(array)):
        if array[item]+array[i]==target_num:
            #final_arr.extend([item,i])
            final_arr="["+str(item)+','+str(i)+']'
            break
print(final_arr)