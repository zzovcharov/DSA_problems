class Solution(object):
    def maxSubsequence(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        max_heap = [(-nums[i], i) for i in range(len(nums))]
        heapq.heapify(max_heap)

        res = []
        for _ in range(k):
            neg_val, idx = heapq.heappop(max_heap)
            res.append((idx, -neg_val))

        res.sort()
        return [val for idx, val in res]