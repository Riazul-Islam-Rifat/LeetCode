# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def pairSum(self, head: [ListNode]) -> int:

        # Dividing the linked list into half
        slow = fast = head

        # Slow indicates the second half
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse the half

        prev = None
        current = slow

        # Reverse the 2nd half
        while current:
            cur_next = current.next
            current.next = prev
            prev = current
            current = cur_next

        # calculate maximum rwin sum

        current1 = head  # [5--4--2--1]
        current2 = prev  # [1--2]
        max_sum = 0
        while current2:
            max_sum = max(max_sum, (current1.val + current2.val))
            current2 = current2.next
            current1 = current1.next

        return max_sum

