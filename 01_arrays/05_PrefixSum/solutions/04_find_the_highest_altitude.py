class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        curr_alt = 0
        max_alt = 0

        for g in gain:
            curr_alt += g
            max_alt = max(max_alt, curr_alt)
        return max_alt