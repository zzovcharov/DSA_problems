class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        for k in range(len(digits)-1, -1, -1):
            if digits[k] < 9:
                digits[k] += 1
                return digits
            else:
                digits[k] = 0
        digits.insert(0, 1)
        return digits