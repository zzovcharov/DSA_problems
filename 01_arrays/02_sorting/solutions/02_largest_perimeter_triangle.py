class Solution(object):
    def largestPerimeter(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Manual sort vs. function
        # if len(nums) < 3:
        #     return 0
        #
        # n = len(nums)
        # for i in range(n):
        #     min_index = i
        #     for j in range(i + 1, n):
        #         if nums[j] < nums[min_index]:
        #             min_index = j
        #     nums[i], nums[min_index] = nums[min_index], nums[i]

        nums.sort()
        n = len(nums)
        for i in range(n - 1, 1, -1):
            a, b, c = nums[i - 2], nums[i - 1], nums[i]
            if a + b > c:
                return a + b + c
        return 0