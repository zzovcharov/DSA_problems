class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n =len(s)

        for k in range(1, n//2 + 1):
            if n % k != 0:
                continue

            block = s[:k]
            times = n//k
            built = block * times

            if built == s:
                return True
        return False