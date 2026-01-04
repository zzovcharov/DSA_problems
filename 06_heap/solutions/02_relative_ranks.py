import heapq
class Solution(object):
    def findRelativeRanks(self, score):
        """
        :type score: List[int]
        :rtype: List[str]
        """
        heap = []
        for i in range(len(score)):
            heapq.heappush(heap, -(score[i], i))
        result = [""] * len(score)
        rank = 1
        while heap:
            neg_score, idx = heapq.heappop(heap)
            if rank == 1:
                result[idx] = "Gold Medal"
            elif rank == 2:
                result[idx] = "Silver Medal"
            elif rank == 3:
                result[idx] = "Bronze Medal"
            else:
                result[idx] = str(rank)
            rank += 1
        return result