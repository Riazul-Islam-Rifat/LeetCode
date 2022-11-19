from collections import deque
from typing import List

class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        queue = deque()
        deck.sort(reverse=True)
        # print(deck)
        # c=0
        for card in deck:
            # c+=1
            if queue:
                # print(queue)
                queue.appendleft(queue.pop())
            queue.appendleft(card)
            # print(c,' ---' , queue)
        return queue