class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        tracker = defaultdict(int)

        for i in arr:
            tracker[i] += 1

        ocr = []

        for key in tracker.keys():
            ocr.append(tracker[key])

        return len(ocr) == len(set(ocr))