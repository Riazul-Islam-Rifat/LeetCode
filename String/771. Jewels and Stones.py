class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        stone_in_jewel = 0
        for item in jewels:
            stone_in_jewel += stones.count(item)

        return stone_in_jewel