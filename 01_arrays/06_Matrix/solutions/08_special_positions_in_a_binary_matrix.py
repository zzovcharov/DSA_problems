class Solution(object):
    def numSpecial(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        row = len(mat)
        col = len(mat[0])


        row_count = [0] * row
        col_count = [0] * col

        for i in range(row):
            for j in range(col):
                if mat[i][j] == 1:
                    row_count[i] += 1
                    col_count[j] += 1

        res = 0
        for i in range(row):
            for j in range(col):
                if mat[i][j] == 1 and row_count[i] ==1 and col_count[j] == 1:
                    res += 1
        return res