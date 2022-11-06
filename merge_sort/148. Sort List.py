# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:

    # Get the middle
    def getMid(self, head):

        if (head == None):
            return head

        slow = fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    # Merge the list
    def mergedList(self, left, right):

        result = None

        if left == None:
            return right

        if right == None:
            return left

        if left.val < right.val:

            result = left
            result.next = self.mergedList(left.next, right)

        else:

            result = right
            result.next = self.mergedList(left, right.next)

        return result

    # Divide and conquer
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head == None or head.next == None:
            return head

        # Get the middle of the linked list
        middle = self.getMid(head)  # Left part
        middleTonext = middle.next  # Right part
        middle.next = None

        # Recursive call
        left = self.sortList(head)
        right = self.sortList(middleTonext)

        sorted_list = self.mergedList(left, right)
        return sorted_list