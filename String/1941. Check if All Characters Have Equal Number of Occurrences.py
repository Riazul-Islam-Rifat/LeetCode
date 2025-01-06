class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        char_dict = Counter(s)
        val_list = char_dict.values()

        return len(set(val_list)) == 1