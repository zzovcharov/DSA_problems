class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        map = set(nums)

        l = len(nums)

        for n in range(l + 1):
            if n not in map:
                return n