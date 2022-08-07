import math


class Solution:
    def countPoints(self, points, queries) -> [int]:
        output = [0] * len(queries)
        count = -1
        for item in queries:
            count += 1
            radius = item[2]
            for i in points:
                euclidean_distance = math.sqrt(((i[0] - item[0]) ** 2) + ((i[1] - item[1]) ** 2))
                if euclidean_distance <= radius:
                    output[count] += 1

        return output