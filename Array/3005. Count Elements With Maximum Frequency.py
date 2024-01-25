class Solution:
    def maxFrequencyElements(self, nums: [int]) -> int:
        freq = {}

        for item in nums:
            if item in freq:
                freq[item] += 1

            else:
                freq[item] = 1

        maxFreq = sorted(freq.items(), key=lambda item: item[1], reverse=True)

        freqs = []

        for i in maxFreq:
            freqs.append(i[1])

        maxVal = freqs.count(freqs[0])

        return maxVal * freqs[0]