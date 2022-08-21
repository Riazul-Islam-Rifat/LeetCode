# Definition for singly-linked list.
from typing import  Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        output=[head] # Appending the head instance first. [First node's location]
        while head:
            if head.next:
                output.append(head.next) # Appending next nodes one by one
            head= head.next

        mid= len(output)//2
        return output[mid]