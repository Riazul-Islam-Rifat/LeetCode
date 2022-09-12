from typing import List

class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:

        # Initializing total time
        total_time = 0

        # For metal garbage collector
        last_idx = 0
        travel_time = 0
        time_for_metal = 0
        for count, item in enumerate(garbage):
            # Count total time to collect all garbage of metals
            time_for_metal += item.count("M")

            # Find the last index which contains metal garbage
            if "M" in item:
                last_idx = count

        # Find the total travel time to collect metal garbage
        if last_idx != 0:  # last_idx is not 0 means at least one house is traveled to collect garbage
            if last_idx < len(travel):
                travel_time = sum(travel[:last_idx])
            else:
                travel_time = sum(travel[::])

        # Total time for metal
        time_for_metal += travel_time

        # print(last_idx)
        # print("Time for metal    ", time_for_metal)

        # For glass garbage collector
        last_idx = 0
        travel_time = 0
        time_for_glass = 0
        for count, item in enumerate(garbage):

            time_for_glass += item.count("G")
            if "G" in item:
                last_idx = count

        if last_idx != 0:
            if last_idx < len(travel):
                travel_time = sum(travel[:last_idx])
            else:
                travel_time = sum(travel[::])

        time_for_glass += travel_time

        # print(last_idx)
        # print("Time for glass    ", time_for_glass)

        # For paper garbage collector
        last_idx = 0
        travel_time = 0
        time_for_paper = 0
        for count, item in enumerate(garbage):

            time_for_paper += item.count("P")
            if "P" in item:
                last_idx = count

        if last_idx != 0:
            if last_idx < len(travel):
                travel_time = sum(travel[:last_idx])
            else:
                travel_time = sum(travel[::])

        time_for_paper += travel_time

        # print(last_idx)
        # print("Time for paper    ", time_for_paper)

        total_time = time_for_paper + time_for_glass + time_for_metal

        return total_time