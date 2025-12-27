class Solution(object):
    def longestAlternatingSubarray(self, nums, threshold):
        """
        :type nums: List[int]
        :type threshold: int
        :rtype: int
        """
        max_len = 0
        i = 0
        n = len(nums)

        while i < n:

            if nums[i] % 2 == 0 and nums[i] <= threshold:
                j = i
                while j < n and nums[j] <= threshold and nums[j] % 2 == (j - i) % 2:
                    j += 1
                max_len = max(max_len, j - i)
                # skip ahead
                i = j
            else:
                i += 1

        return max_len