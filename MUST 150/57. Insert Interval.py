from typing import List
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # Time and space complexity O(n)
        if len(intervals)==0:
            return [newInterval]
        finalInterval = []
        flag = False # To track the insertion of the newInterval
        for  curInterval in intervals:
            # 1Index is ending time 0Index is starting time
            if curInterval[1]<newInterval[0]: # CurInterval is smaller than the newInterval
                finalInterval.append(curInterval)
            elif newInterval[1]<curInterval[0]: # CurInterval is greater than the newInterval
                # First we add the newInterval and then add the curInterval
                if not flag:
                    flag = True
                    finalInterval.append(newInterval)
                    finalInterval.append(curInterval)
                else: # When current interval is already inserted
                    finalInterval.append(curInterval)
            else: # When curInterval overlaps with the newInterval, we merge two intervals and update the newInterval
                newInterval[0],newInterval[1] = min(newInterval[0],curInterval[0]), max(newInterval[1],curInterval[1])
        if not flag:
            finalInterval.append(newInterval)
        return finalInterval

