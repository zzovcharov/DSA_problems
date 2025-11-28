class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        for k in range(len(flowerbed)):
            if flowerbed[k] == 0:
                empty_l = (k == 0) or flowerbed[k - 1] == 0
                empty_r = (k == len(flowerbed) - 1) or flowerbed[k + 1] == 0
                if empty_l and empty_r:
                    flowerbed[k] = 1
                    n -= 1
                    if n == 0:
                        return True
        return n <= 0