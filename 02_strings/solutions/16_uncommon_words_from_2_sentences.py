class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        words1 = s1.split()
        words2 = s2.split()
        res = []

        seen1 = {}
        for word in words1:
            if word in seen1:
                seen1[word] += 1
            else:
                seen1[word] = 1
        seen2 = {}
        for word in words2:
            if word in seen2:
                seen2[word] += 1
            else:
                seen2[word] = 1
        for word in seen1:
            if seen1[word] == 1 and word not in seen2:
                res.append(word)
        for word in seen2:
            if seen2[word] == 1 and word not in seen1:
                res.append(word)

        return res
