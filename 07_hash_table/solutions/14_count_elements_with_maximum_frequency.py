class Solution(object):
    def maxFrequencyElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq = {}

        for f in nums:
            freq[f] = freq.get(f,0) + 1

        maxFreq = max(freq.values())
        total = 0

        for c in freq.values():
            if c == maxFreq:
                total += c
        return total