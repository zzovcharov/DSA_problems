class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        n =len(mat)
        total = 0

        for i in range(n):
            # 1st diagonal
            total += mat[i][i]

            if i != n - 1 -i:
                total += mat[i][n - 1 -i]
        return total