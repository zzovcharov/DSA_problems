class Solution(object):
    def longestNiceSubstring(self, s):
        """
        :type s: str
        :rtype: str
        """
        def is_nice(sub):
            chars = set(sub)
            for ch in chars:
                if ch.swapcase() not in chars:
                    return False
            return True

        def helper(s):
            if len(s) < 2:
                return ""
            chars = set(s)
            for i, ch in enumerate(s):
                if ch.swapcase() not in chars:
                    left = helper(s[:i])
                    right = helper(s[i + 1:])
                    return left if len(left) >= len(right) else right
            return s

        return helper(s)