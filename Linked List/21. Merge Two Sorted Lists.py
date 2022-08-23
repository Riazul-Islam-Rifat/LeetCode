# Definition for singly-linked list.
from typing import  Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        merged_list = ListNode()
        dummy = merged_list

        while list1 and list2:
            if list1.val < list2.val:
                dummy.next = ListNode(list1.val)
                list1 = list1.next
            elif list1.val >= list2.val:
                dummy.next = ListNode(list2.val)
                list2 = list2.next
            dummy = dummy.next

        if not list1:
            dummy.next = list2
        if not list2:
            dummy.next = list1

        return merged_list.next