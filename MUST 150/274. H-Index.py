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

    # Example:
    # citations = [3, 0, 6, 1, 5]
    # sort in reversed - 6 5 3 1 0
    # index              0 1 2 3 4