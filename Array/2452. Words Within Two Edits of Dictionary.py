class Solution:
    def twoEditWords(self, queries: [str], dictionary: [str]) -> [str]:
        n = 0
        output = []
        for item in queries:
            if item in dictionary:
                output.append(item)

            else:
                item_list = list(item)
                for i in dictionary:
                    i_list = list(i)
                    count = 0
                    for j in range(len(i_list)):
                        if i_list[j] != item_list[j]:
                            i_list[j] = item_list[j]
                            count += 1
                    if count <= 2 and item_list == i_list:
                        if item not in output:
                            output.append(item)

        return output