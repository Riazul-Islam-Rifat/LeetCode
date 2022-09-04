# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        l1, l2 = list1, list2

        for i in range(a - 1):
            l1 = l1.next

        merge = l1.next
        l1.next = list2

        for j in range(b - a + 1):
            merge = merge.next

        while l2.next:
            l2 = l2.next
        l2.next = merge

        return list1

        #####        #####
#         current= list1
#         current2=list1
#         current3=list2
#         merge= None

#         while current2.next:
#             if current2.next.val==b:
#                 merge=ListNode(current2.next.next.val,current2.next.next.next)
#             current2=current2.next

#         while current3:
#             if current3.next is None:
#                 current3.next=merge
#                 break
#             else:
#                 current3=current3.next

#         while current.next:
#             if current.next.val==a:
#                 current.next=list2
#             current=current.next

#         return list1