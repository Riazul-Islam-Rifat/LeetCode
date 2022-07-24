boxes=input('Enter Boxes -- ')
answer=[0]*len(boxes)
for pos,val in enumerate(boxes):
    for item in range(len(boxes)-1,-1,-1):
        if val=='1':
            answer[item]+=abs(pos-item)
print(answer)