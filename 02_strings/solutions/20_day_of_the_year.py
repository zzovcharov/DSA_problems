class Solution(object):
    def dayOfYear(self, date):
        """
        :type date: str
        :rtype: int
        """
        y, m, d = map(int, date.split("-"))
        month = [31,28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        for i in range(1, m):
            d += month[i-1]

        # leap year adjustment
        if (y % 400 == 0 or (y % 4 ==0 and y % 100 != 0)) and m> 2:
            d += 1

        return d