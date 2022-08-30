# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeNodes(self, head: [ListNode]) -> [ListNode]:

        current = head  # currenr and head shares the same address

        # The following while condition stisfies when there are at least one value in between two 0s. [0,1,0]/[0,1,2,0,3,0]
        while current and current.next.next:
            # Add the non zero value and update the next
            if current.next.val != 0:
                current.val += current.next.val
                current.next = current.next.next  # for [0,1,0] current.next indicates the last 0.
            else:
                # when the next value is not zero we simply forward to the next
                current = current.next

        current.next = None  # Eliminate the last 0 from linked list

        return head