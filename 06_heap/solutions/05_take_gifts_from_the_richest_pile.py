class Solution(object):
    def pickGifts(self, gifts, k):
        """
        :type gifts: List[int]
        :type k: int
        :rtype: int
        """
        max_heap = [-n for n in gifts]
        heapq.heapify(max_heap)

        while k:
            left = math.isqrt(-heapq.heappop(max_heap))
            heapq.heappush(max_heap, -left)
            k -= 1
        return -sum(max_heap)