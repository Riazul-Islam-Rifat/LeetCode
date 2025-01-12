# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:

        # Store in a list
        tracker = []

        def inOrder(root):
            if root:
                inOrder(root.left)
                tracker.append(root.val)
                inOrder(root.right)

        inOrder(root)

        # print(tracker)
        # Binary search
        def nodes(tracker, n):
            left = 0
            right = len(tracker) - 1

            mini = -1
            maxi = -1

            while left <= right:
                mid = (left + right) // 2
                if tracker[mid] == n:
                    return [tracker[mid], tracker[mid]]

                elif n < tracker[mid]:
                    maxi = tracker[mid]
                    right = mid - 1

                else:
                    left = mid + 1
                    mini = tracker[mid]

            return [mini, maxi]

        return [nodes(tracker, i) for i in queries]