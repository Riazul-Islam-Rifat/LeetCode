# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        tracker = []
        while head:
            tracker.append(head.val)
            head = head.next

        def helper(l, r, t):

            if l > r:
                return None

            m = (l + r) // 2
            root = TreeNode(t[m])
            root.left = helper(l, m - 1, t)
            root.right = helper(m + 1, r, t)

            return root

        return helper(0, len(tracker) - 1, tracker)