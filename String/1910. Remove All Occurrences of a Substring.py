class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:

        for item in range(len(s)):
            # if part in s then we replace it with ""
            # We replace one occurance at a time from left
            if part in s:
                s = s.replace(part, "", 1)

            else:
                # Else we terminate the loop
                break

                # At last we return the updated s
        return s