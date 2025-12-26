class Solution(object):
    def average(self, salary):
        """
        :type salary: List[int]
        :rtype: float
        """
        salary.sort()
        middle = salary[1:-1]
        #avg
        return float(sum(middle)) / len(middle)