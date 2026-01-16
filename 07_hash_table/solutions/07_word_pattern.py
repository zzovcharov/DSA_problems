class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        words = s.split(" ")

        if len(pattern) != len(words):
            return False

        charToWords = {}
        usedWords = set()

        for c, w in zip(pattern, words):
            if c in charToWords:
                if charToWords[c] != w:
                    return False
            else:
                if w in usedWords:
                    return False
                charToWords[c] = w
                usedWords.add(w)
        return True