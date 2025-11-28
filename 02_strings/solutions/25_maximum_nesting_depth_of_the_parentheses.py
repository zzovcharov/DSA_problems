class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        current = 0
        max  = 0

        for ch in s:
            if ch == '(':
                current += 1
                if current > max:
                    max = current
            elif ch == ')':
                current -= 1
        return max