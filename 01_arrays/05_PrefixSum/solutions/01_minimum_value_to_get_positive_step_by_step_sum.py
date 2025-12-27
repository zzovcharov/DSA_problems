class Solution(object):
    def minStartValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = 0
        min_sum = 0

        for num in nums:
            total += num
            min_sum = min(total, min_sum)
        return 1 - min_sum if min_sum < 0 else 1