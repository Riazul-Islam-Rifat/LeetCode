# Definition for singly-linked list.
from typing import  Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None

        current = head

        while current:
            next_elem = current.next  # Storing the next node in next_elem
            current.next = prev  # The previous nodes becomes the next node here [reversing]
            prev = current  # updating the prev node in every iteration
            current = next_elem  # Updating the current element

        return prev