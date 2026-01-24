class Solution(object):
    def getCommon(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        set1= set(nums1)
        set2 = set(nums2)

        common = set1 & set2

        if not common:
            return -1
        return min(common)