class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        ban = set(banned)
        words = re.findall(r"[a-z]+", paragraph.lower())

        freq = {}
        bestWord = ""
        bestCount = 0

        for w in words:
            if w in ban:
                continue
            freq[w] = freq.get(w, 0) + 1
            if freq[w] > bestCount:
                bestWord = w
                bestCount = freq[w]
        return bestWord