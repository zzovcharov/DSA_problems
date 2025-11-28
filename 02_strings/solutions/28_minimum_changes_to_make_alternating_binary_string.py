class Solution(object):
    def minOperations(self, s):
        """
        :type s: str
        :rtype: int
        """
        diffA = 0
        diffB = 0

        for i, ch in enumerate(s):
            expA = '0' if i % 2 == 0 else '1'
            expB = '1' if i % 2 ==0 else '0'

            if ch != expA:
                diffA += 1
            if ch != expB:
                diffB += 1
        return min(diffA, diffB)

