class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        countM = {}

        for ch in magazine:
            countM[ch] =countM.get(ch, 0) + 1

        for c in ransomNote:
            if c in countM and countM[c] > 0:
                countM[c] -= 1
            else:
                return False
        return True
