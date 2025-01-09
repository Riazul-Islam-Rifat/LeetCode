class Solution:
    def isPossible(self, nums: List[int]) -> bool:

        if len(nums) < 3:
            return False

        freq = collections.Counter(nums)
        subseq = collections.defaultdict(int)

        for i in nums:
            if freq[i] == 0:
                continue
            # print(i,"This the number")
            freq[i] -= 1
            # print(subseq[i-1],'subses prev name')
            # Add to an existing sequence
            if subseq[i - 1] > 0:
                subseq[i - 1] -= 1
                subseq[i] += 1
                # print(subseq, "This is existing one")

            # create a new subseq
            elif freq[i + 1] and freq[i + 2]:
                freq[i + 1] -= 1
                freq[i + 2] -= 1
                subseq[i + 2] += 1
                # print(subseq, "This is new one")

            else:
                return False

        return True


