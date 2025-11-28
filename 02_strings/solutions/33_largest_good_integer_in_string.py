class Solution(object):
    def largestGoodInteger(self, num):
        """
        :type num: str
        :rtype: str
        """
        res = ""
        for i in range(len(num)- 2):
            block = num[i: i + 3]
            if block[0] == block[1] == block[2]:
                if block > res:
                    res = block
        return res