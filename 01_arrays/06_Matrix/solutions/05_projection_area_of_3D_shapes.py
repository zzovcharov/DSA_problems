class Solution(object):
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # count all cells from top
        # track max of each row and column

        n = len(grid)
        top = 0
        front = 0
        side = 0

        for i in range(n):
            row_max = 0
            col_max = 0
            for j in range(n):
                if grid[i][j] > 0:
                    top += 1
                row_max = max(row_max, grid[i][j])
                col_max = max(col_max, grid[j][i])
            side += row_max
            front += col_max

        return top + front + side