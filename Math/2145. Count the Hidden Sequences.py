class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        l, u = lower, upper
        for diff in differences:
            l, u = max(lower, l + diff), min(upper, u + diff)
            if l > upper or u < lower:
                return 0

        return u - l + 1

