class Solution(object):
    def numberOfLines(self, widths, s):
        """
        :type widths: List[int]
        :type s: str
        :rtype: List[int]
        """
        line = 1
        curr_w = 0

        for i in s:
            index_w = widths[ord(i) - ord('a')]
            if curr_w + index_w > 100:
                line += 1
                curr_w = index_w
            else:
                curr_w += index_w
        return [line, curr_w]

