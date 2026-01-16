class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        freq = {}

        for i, n in enumerate(nums):
            if n in freq and i - freq[n] <= k:
                return True
            freq[n] = i
        return False