class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> list:
        freq = {}
        res = []
        words = (s1 + " " + s2).split()

        for w in words:
            freq[w] = freq.get(w, 0) + 1
        for w in words:
            if freq[w] == 1:
                res.append(w)
        return res