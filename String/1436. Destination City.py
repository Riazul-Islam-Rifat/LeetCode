class Solution:
    def destCity(self, paths: [[str]]) -> str:

        tracker = {}

        for item in paths:
            for i in item:
                if i not in tracker.keys():
                    tracker[i] = item.index(i)

                else:
                    tracker[i] = False

        for key, value in tracker.items():
            if value == 1:
                return key