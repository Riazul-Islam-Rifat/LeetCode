class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Time complexity: O(nlogn)
        # Space complexity: O(n)
        # Sort the input array based on it's first element so that we get the sorted starting time
        sortedIntervals = sorted(intervals, key=lambda x: x[0])

        currentInterval = sortedIntervals[0]
        mergedIntervals = [currentInterval]

        for nextInterval in sortedIntervals:

            if currentInterval[1] >= nextInterval[0]:  # Means currentInterval and nextInterval are overlapping
                # So we merge these two intervals
                currentInterval[1] = max(currentInterval[1], nextInterval[1])  # We take the max ending

            else:  # We add the nextInterval to the mergedIntervals
                mergedIntervals.append(nextInterval)
                # Update the currentInterval
                currentInterval = nextInterval

        return mergedIntervals
