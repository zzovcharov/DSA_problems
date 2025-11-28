class Solution(object):
    def destCity(self, paths):
        """
        :type paths: List[List[str]]
        :rtype: str
        """
        start_city = set()

        for a, b in paths:
            start_city.add(a)
        for a, b in paths:
            if b not in start_city:
                return b