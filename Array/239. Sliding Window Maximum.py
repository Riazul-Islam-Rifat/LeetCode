class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0
        output = []
        q = collections.deque()

        for r in range(len(nums)):
            while len(q) != 0 and q[-1] < nums[r]:
                q.pop()

            q.append(nums[r])

            if r - l + 1 == k:
                output.append(q[0])

                if q[0] == nums[l]:
                    q.popleft()
                l += 1

        return output