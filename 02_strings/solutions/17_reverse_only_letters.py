class Solution(object):
    def reverseOnlyLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        r = []

        letters = [ch for ch in s if ch.isalpha()]
        letters.reverse()

        for ch in s:
            if ch.isalpha():
                r.append(letters.pop(0))
            else:
                r.append(ch)

        return ''.join(r)
