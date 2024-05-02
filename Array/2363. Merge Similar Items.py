class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        ret = []
        addedItem = []
        # Applying non-optimal solution

        for item in items1:
            val1 = item[0]
            weight1 = item[1]
            boolean = False
            for item2 in items2:
                val2 = item2[0]
                if val1 == val2:
                    totalWeight = weight1 + item2[1]
                    ret.append([val1,totalWeight])
                    boolean = True
            if not boolean:
                ret.append([val1,weight1])

        for item2 in items2:
            val2 = item2[0]
            weight2 = item2[1]
            boolean = False
            for item in items1:
                val1 = item[0]
                if val1 == val2:
                    boolean = True
            if not boolean:
                ret.append([val2,weight2])

        return sorted(ret,key= lambda x: x[0])