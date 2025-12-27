class Solution(object):
    def largestLocal(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[List[int]]
        """
        rows = len(grid)
        cols = len(grid[0])

        res = [[0] * (cols - 2) for _ in range(rows - 2)]


        for r in range(rows- 2):
            for c in range(cols - 2):
                max_num = 0
                for i in range(r, r + 3):
                    for j in range(c, c + 3):
                        max_num = max(max_num, grid[i][j])
                res[r][c] = max_num
        return res