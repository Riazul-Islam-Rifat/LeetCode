# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        if head:
            current = head
            current.val = 'T'

            while current.next:
                if current.next.val == 'T':
                    return True
                current.val = 'T'
                current = current.next

        return False
