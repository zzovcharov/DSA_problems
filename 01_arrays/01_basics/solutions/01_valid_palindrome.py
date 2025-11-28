class Solution(object):
    def isPalindrome(self, s: str) -> bool:
        """
        :type s: str
        :rtype: bool
        """
        clean = ''
        for char in s:
            if char.isalnum():
                clean += char.lower()
        return clean == clean[::-1]
