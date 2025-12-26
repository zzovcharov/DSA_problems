class Solution(object):
    def maxProductDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        arr = nums[:]
        arr.sort()

        max1, max2 = arr[-1], arr[-2]
        min1, min2 = arr[0], arr[1]

        return (max1 * max2) - (min1 * min2)