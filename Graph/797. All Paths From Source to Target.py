from typing import List

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:

        end_of_graph = len(graph) - 1

        def find_path(node, path, output):
            if node == end_of_graph:
                output.append(path)

            for item in graph[node]:
                find_path(item, path + [item], output)

        output = []
        find_path(0, [0], output)

        return output

    # Path becomes [0] when a whole iteration is completely done for a single item of graph[node]
# Ekta item theke onno node e gele oi node er for loop execute houar shomoy end node pele path hobe [0] +[item] .. but oi item theke end node pele path hobe [0]
