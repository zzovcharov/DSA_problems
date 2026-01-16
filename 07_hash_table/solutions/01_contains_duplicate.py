class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        countMap = {}
        for n in nums:
            if n in countMap:
                return True   # duplicate found
            countMap[n] = 1
        return False

# Alternative Sol
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))
