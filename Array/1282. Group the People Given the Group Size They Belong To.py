class Solution:
    def groupThePeople(self, groupSizes):
        grp_dict={}
        for count,val in enumerate(groupSizes):
            if val in grp_dict:
                grp_dict[val].append(count)

            else:
                grp_dict[val]=[count]

        #print(grp_dict)

        output_list=[]
        track_list=[]

        for key,item in grp_dict.items():
            for i in range(0,len(item),key):
                output_list.append(item[i:key+i])

        return output_list
