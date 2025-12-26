class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        merged = []
        i = 0

        #merge
        while i < len(word1) and i < len(word2):
            merged.append(word1[i])
            merged.append(word2[i])
            i += 1

        #append the remaining part
        if i < len(word1):
            merged.append(word1[i:])
        if i < len(word2):
            merged.append(word2[i:])
        return ''.join(merged)

