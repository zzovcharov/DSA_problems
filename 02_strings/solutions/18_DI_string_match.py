class Solution(object):
    def diStringMatch(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        n = len(s)
        res = list(range(n + 1))
        i = 0

        while i < n:
            if s[i] == 'D':
                j = i
                while j < n and s[j] == 'D':
                    j += 1
                res[i:j+1] = reversed(res[i:j+1])
                i = j
            else:
                i += 1
        return res