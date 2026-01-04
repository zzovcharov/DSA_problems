class Solution(object):
    def numberGame(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        arr = []
        heapq.heapify(nums)

        while nums:
            A = heapq.heappop(nums)
            B = heapq.heappop(nums)
            arr.append(B)
            arr.append(A)
        return arr