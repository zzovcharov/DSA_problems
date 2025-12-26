class Solution(object):
    def buyChoco(self, prices, money):
        """
        :type prices: List[int]
        :type money: int
        :rtype: int
        """
        prices.sort()
        total_cost = prices[0] + prices[1]

        if total_cost <= money:
            return money - total_cost
        else:
            return money