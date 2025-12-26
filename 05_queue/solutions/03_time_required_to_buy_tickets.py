from collections import deque

class Solution(object):
    def timeRequiredToBuy(self, tickets, k):
        """
        :type tickets: List[int]
        :type k: int
        :rtype: int
        """
        time = 0
        q = deque()

        for i in range(len(tickets)):
            q.append((tickets[i], i))
        while q:
            tickets_left, idx = q.popleft()
            tickets_left -= 1
            time += 1
            if idx == k and tickets_left == 0:
                return time
            if tickets_left > 0:
                q.append((tickets_left, idx))