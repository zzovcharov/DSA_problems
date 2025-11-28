class Solution(object):
    def isPathCrossing(self, path):
        """
        :type path: str
        :rtype: bool
        """
        x, y = (0, 0)
        observed = {(0, 0)}

        for ch in path:
            if ch == 'N':
                y += 1
            elif ch == 'S':
                y -= 1
            elif ch == 'E':
                x += 1
            else:
                x -= 1

            pos = (x, y)
            if pos in observed:
                return True
            observed.add(pos)

        return False