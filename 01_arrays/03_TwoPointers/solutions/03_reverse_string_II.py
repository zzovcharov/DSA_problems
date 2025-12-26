class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        result = ""
        i = 0
        while i < len(s):
            # take the next 2k chunk
            chunk = s[i:i + 2 * k]
            first_k = chunk[:k][::-1]
            rest = chunk[k:]
            # add two parts together
            result += first_k + rest
            # move to the next 2k chunk
            i += 2 * k
        return result