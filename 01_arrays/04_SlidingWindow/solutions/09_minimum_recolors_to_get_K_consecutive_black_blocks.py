class Solution(object):
    def minimumRecolors(self, blocks, k):
        """
        :type blocks: str
        :type k: int
        :rtype: int
        """
        current_w = blocks[:k].count('W')
        min_ops = current_w

        for i in range(k, len(blocks)):
            if blocks[i - k] == 'W':
                current_w -= 1
            if blocks[i] == 'W':
                current_w += 1
            min_ops = min(min_ops, current_w)

        return min_ops