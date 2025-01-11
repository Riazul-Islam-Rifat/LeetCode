class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Bucket sort [modified]
        count = collections.defaultdict(int)
        for i in nums:
            count[i]+=1

        freq = [[] for i in range(len(nums)+1)]

        for val, freqs in count.items():
            freq[freqs].append(val)

        res = []

        for i in range(len(freq)-1,0,-1):
            for j in freq[i]:
                res.append(j)
                if len(res)==k:
                    return res