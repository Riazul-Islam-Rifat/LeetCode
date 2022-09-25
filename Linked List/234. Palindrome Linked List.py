# Definition for singly-linked list.
from typing import  Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        # Initializig a string named linked_val
        linked_val = ''

        # Initializing a boolean value
        flag = False

        # Traversing the linked list and storing it's value in linked_val

        while head:
            linked_val += str(head.val)
            head = head.next

        # When there is a single value in linked_list return True
        if len(linked_val) == 1:
            return True

        # If the first half of linked_val is same as the reversed 2nd half linked_val then it's palindrome.
        if len(linked_val) % 2 == 0:
            if linked_val[:(len(linked_val) // 2)] == linked_val[(len(linked_val) // 2)::][::-1]:
                return True

        else:
            if (linked_val[:(len(linked_val) // 2) + 1]) == (linked_val[(len(linked_val) // 2)::][::-1]):
                return True

        return flag