class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)
        p = [0] * (n + 1)
        for i in range(n):
            p[i+1] = p[i] + arr[i]

        total = 0
        #try all odd lengths
        for l in range(1, n + 1,2):
            for start in range (n - l + 1):
                end = start + l
                sub_sum = p[end] - p[start]
                total += sub_sum

        return total
