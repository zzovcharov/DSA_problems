class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        orig_color = image[sr][sc]
        if orig_color == color:
            return image

        rows = len(image)
        cols = len(image[0])
        queue = [(sr, sc)]

        while queue:
            r, c = queue.pop(0)
            if image[r][c] == orig_color:
                image[r][c] = color

                # check neighbors
                if r > 0 and image[r - 1][c] == orig_color:
                    queue.append((r - 1, c))
                if r < rows - 1 and image[r + 1][c] == orig_color:
                    queue.append((r + 1, c))
                if c > 0 and image[r][c - 1] == orig_color:
                    queue.append((r, c - 1))
                if c < cols - 1 and image[r][c + 1] == orig_color:
                    queue.append((r, c + 1))

        return image
