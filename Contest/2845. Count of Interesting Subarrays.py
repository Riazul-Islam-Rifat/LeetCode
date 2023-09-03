from collections import Counter
class Solution:
    # Time complexity: O(n)
    def countInterestingSubarrays(self, A: [int], mod: int, k: int) -> int:
        res = acc = 0
        count = Counter({0: 1})
        for a in A:
            acc = (acc + (1 if a % mod == k else 0)) % mod
            res += count[(acc - k) % mod]
            count[acc] += 1
        return res