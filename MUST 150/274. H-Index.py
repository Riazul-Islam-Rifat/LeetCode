class Solution:
    def hIndex(self, citations: [int]) -> int:
        citations.sort(reverse=True)

        res = 0

        for idx, val in enumerate(citations):
            if val<=idx:
                return idx

        return len(citations)

    # Time complexity: O(nlogn)
    # Space complexity: O(1)