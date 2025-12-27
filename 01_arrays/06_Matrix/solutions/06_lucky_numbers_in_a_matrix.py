class Solution(object):
    def luckyNumbers (self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        m = len(matrix)
        n = len(matrix[0])
        result = []

        for i in range(m):
            row_min = min(matrix[i])
            col_index = matrix[i].index(row_min)

            col_max = max(matrix[r][col_index] for r in range(m))

            if row_min ==col_max:
                result.append(row_min)
        return result