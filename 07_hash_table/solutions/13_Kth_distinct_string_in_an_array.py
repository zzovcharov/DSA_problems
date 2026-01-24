class Solution(object):
    def kthDistinct(self, arr, k):
        """
        :type arr: List[str]
        :type k: int
        :rtype: str
        """
        freq = {}
        count = 0

        for s in arr:
            freq[s] = freq.get(s, 0) + 1
        for s in arr:
            if freq[s] == 1:
                count += 1
                if count == k:
                    return s
        return ""
