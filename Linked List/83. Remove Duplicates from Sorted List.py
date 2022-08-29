# Definition for singly-linked list.
from typing import  Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return

        curr = head  # curr will be updated, head will be returned

        while curr and curr.next:
            if curr.val == curr.next.val:
                # Here updating curr.next to delete the duplicate value duplicate.
                # curr stays as same as the present one but the next address is updated
                curr.next = curr.next.next

            else:
                # When if condition is not satisfied the current value becomes the next value
                curr = curr.next

        return head