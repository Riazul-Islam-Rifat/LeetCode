from typing import  Optional
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        lenA = lenB = 0
        # Storing headA and headB in separate variable
        Ahead = headA
        Bhead = headB

        # Finding  length headA and headB
        while headA or headB:
            if headA:
                lenA += 1
                headA = headA.next

            if headB:
                lenB += 1
                headB = headB.next

        # initializing long as headA when headA's lenght (lenA) in max and short is initialized as headB
        if lenA >= lenB:
            long = Ahead
            short = Bhead
        # initializing long as headB when headB's lenght (lenB) in max and short is initialized as headA
        else:
            long = Bhead
            short = Ahead

        for item in range(abs(lenA - lenB)):
            long = long.next

        while long:
            if long == short:
                return long

            long = long.next

            short = short.next

        return None