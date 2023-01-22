class Solution:
    def reverseWords(self, s: str) -> str:
        s_list = s.split(' ')
        tracker = []
        for item in s_list:
            tracker.append(item[::-1])

        return ' '.join(tracker)
