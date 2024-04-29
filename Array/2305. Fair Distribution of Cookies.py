class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        distribution = [0] * k
        minUnfair = float('inf')

        def backTrack(bag):
            nonlocal distribution, minUnfair
            if bag == len(cookies):  # Base case
                minUnfair = min(minUnfair, max(distribution))  # Update the minUnfair
                return

            if minUnfair < max(distribution):
                return

            for i in range(k):
                distribution[i] += cookies[bag]  # Distribute the bag to a child
                backTrack(bag + 1)  # Goes for the next bag
                distribution[i] -= cookies[bag]  # Take back from the child

        backTrack(0)
        return minUnfair
