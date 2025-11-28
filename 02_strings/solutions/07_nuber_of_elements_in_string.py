class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        k = s.split()
        return len(k)