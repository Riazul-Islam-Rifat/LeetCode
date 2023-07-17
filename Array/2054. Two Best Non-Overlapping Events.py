class Solution:
    def maxTwoEvents(self, events: [[int]]) -> int:
        tracker = []
        res = 0
        CurrentMaxVal = 0  # Max value of finished events so far

        for start, end, val in events:
            tracker.append([start, True, val])  # Starting time, started, value
            tracker.append([end + 1, False, val])  # End time (inclusive), ended, value

        print(tracker)

        tracker.sort()  # Sort according to starting time

        print(tracker)

        for time, is_start, val in tracker:
            if is_start:
                res = max(res, CurrentMaxVal + val)
            else:
                CurrentMaxVal = max(CurrentMaxVal, val)
        return res
