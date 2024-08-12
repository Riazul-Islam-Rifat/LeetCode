class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        # The solution below is O(n) time as it never iterates same element n*n times.
        # First find a peak and then go left and right
        # The first and last element can't be peak as there will be no left and right value

        mountain = 0

        for i in range(1, len(arr) - 1):
            currentMountain = 0
            if arr[i - 1] < arr[i] and arr[i] > arr[i + 1]:
                # We have found a peak

                peak = i

                while peak > 0 and arr[peak - 1] < arr[peak]:  # Check left
                    currentMountain += 1
                    peak -= 1

                peak = i
                while peak < len(arr) - 1 and arr[peak] > arr[peak + 1]:  # Check right
                    currentMountain += 1
                    peak += 1

            # Handle the no mountain case as well
            mountain = max(mountain, currentMountain + 1) if currentMountain != 0 else max(mountain, currentMountain)

        return mountain

