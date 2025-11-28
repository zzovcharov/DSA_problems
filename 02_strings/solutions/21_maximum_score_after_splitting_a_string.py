class Solution(object):
    def maxScore(self, s):
        """
        :type s: str
        :rtype: int
        """
        zeros_left = 0
        ones_right = s.count('1')
        max_score = 0

        for i in range(len(s) - 1):
            if s[i] == '0':
                zeros_left += 1
            else:  # s[i] == '1'
                ones_right -= 1

            max_score = max(max_score, zeros_left + ones_right)

        return max_score
