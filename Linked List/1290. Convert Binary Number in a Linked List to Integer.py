# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head) -> int:
        if head is None:
            return
        binary = ''
        while head:
            binary += str(head.val)
            head = head.next

        decimal = int(binary, 2)
        return decimal