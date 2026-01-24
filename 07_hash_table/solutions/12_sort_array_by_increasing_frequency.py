class Solution(object):
    def frequencySort(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        freq= {}

        for n in nums:
            freq[n] = freq.get(n, 0) + 1
        return sorted(nums, key = lambda x: (freq[x], -x))