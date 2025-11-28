class Solution(object):
    def largeGroupPositions(self, s):
        r = []
        n = len(s)
        start = 0
        i = 0

        while i < n:
            while i < n and s[i] == s[start]:
                i += 1

            length = i - start
            if length >= 3:
                r.append([start, i - 1])

            start = i

        return r
