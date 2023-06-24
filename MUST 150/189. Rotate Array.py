class Solution:
    def rotate(self, arr: [int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Time O(n) and space O(1)
        k = k%len(arr)
        arr[0:k],arr[k:len(arr)] = arr[len(arr)-k:len(arr)],arr[0:len(arr)-k]

        # We can also use the reverse approach.
        # First we reverse the array
        # Then we re-reverse 2 portions of the array. 0 to k and k to len(arr).