class Solution:
    def countDistinctIntegers(self, nums: [int]) -> int:
        # Initializing a set to store distinct number
        num = set(nums)

        for item in nums:
            # Convert the item into string
            str_item = str(item)

            # Reverse the item
            reverse_item = "".join(reversed(str_item))
            # reverse_item = str_item[::-1]

            # add int of item in mun
            num.add(int(reverse_item))

        return len(num)