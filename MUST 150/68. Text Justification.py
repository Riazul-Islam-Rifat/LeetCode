class Solution:
    def fullJustify(self, words: [str], maxWidth: int) -> [str]:
        res, line, width = [], [], 0

        for w in words:
            if width + len(w) + len(line) > maxWidth:
                for i in range(maxWidth - width):
                    line[i % max(len(line) - 1 , 1)] += ' '
                res, line, width = res + [''.join(line)], [], 0
            line += [w]
            width += len(w)

        return res + [' '.join(line).ljust(maxWidth)]

    # Time complexity: O(n)
    # Space complexity: O(n*m)