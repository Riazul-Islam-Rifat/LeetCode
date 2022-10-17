from typing import List

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:

        # Creating a dictionary using names and heights
        person_dict = {}

        for item in range(len(heights)):
            person_dict[heights[item]] = names[item]

        # Sorting according to height
        sorted_height = sorted(person_dict, reverse=True)

        # Initializing a list to store sorted names
        names = []
        for item in sorted_height:
            names.append(person_dict[item])

        return names