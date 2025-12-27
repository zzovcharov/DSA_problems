class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # counting frequencies
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        # search harmonious sequencies
        max_len = 0
        for num in freq:
            if num + 1 in freq:
                max_len = max(max_len, freq[num] + freq[num + 1])
        return max_len