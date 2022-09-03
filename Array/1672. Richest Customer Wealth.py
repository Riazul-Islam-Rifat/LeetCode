class Solution:
    def maximumWealth(self, accounts: [[int]]) -> int:
        max_wealth=0
        for item in range(len(accounts)):
            max_wealth= max((sum(accounts[item])),max_wealth)
        return max_wealth