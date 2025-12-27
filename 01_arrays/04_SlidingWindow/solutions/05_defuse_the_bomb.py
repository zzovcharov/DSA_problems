class Solution(object):
    def decrypt(self, code, k):
        """
        :type code: List[int]
        :type k: int
        :rtype: List[int]
        """
        n = len(code)
        result = []

        for i in range(n):
            total = 0
            if k == 0:
                total = 0
            elif k > 0:
                for j in range(1, k + 1):
                    total += code[(i + j) % n]
            else:
                for j in range(1, -k + 1):
                    total += code[(i - j) % n]
            result.append(total)

        return result