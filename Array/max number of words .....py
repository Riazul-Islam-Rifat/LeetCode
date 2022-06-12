def max_num(inpt_list):
    sentences=inpt_list
    max_ = 0
    max_word = 0
    for item in range(len(sentences)):
        s_list = sentences[item].split(' ')
        length = len(s_list)
        max_word = max(max_, length)
        max_ = max_word
    return max_word

inpt_list=[]
num_of_sentence=int(input())
for item in range(num_of_sentence):
    inpt = input()
    inpt_list.append(inpt)
result=max_num(inpt_list)
print(result)