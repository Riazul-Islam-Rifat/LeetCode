class Solution:
    def defangIPaddr(self, address: str) -> str:
        # replace all . with [.]
        updated_add = address.replace(".", "[.]")
        return updated_add