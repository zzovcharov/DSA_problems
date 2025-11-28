class Solution(object):
    def maxPower(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == "":
            return 0

        curr = 1
        best = 1
        prev = s[0]

        for ch in s[1:]:
            if ch == prev:
                curr += 1
            else:
                curr = 1
                prev = ch

            best  = max(best, curr)
        return best