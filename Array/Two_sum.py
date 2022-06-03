# With time complexity o(n)
def twoSum(arr,target):
    tracker={}
    for index, value in enumerate(arr):
        difference=target-value
        if difference in tracker:
            return [tracker[difference],index]
        tracker[value]=index

inpt = input()
target= int(input())
array=list(map(int,inpt.split()))
result=twoSum(array,target)
print(result)


# With o(n^2) time complexity.

'''given_arr=input()
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
print(final_arr)'''