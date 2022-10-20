class Solution:
    def decode(self, encoded: [int], first: int) -> [int]:
        # Initializing output list
        output = [first]

        # If a xor b = c then a = b xor c
        for item in range(len(encoded)):
            original_item = encoded[item] ^ output[item]
            output.append(original_item)

        return output