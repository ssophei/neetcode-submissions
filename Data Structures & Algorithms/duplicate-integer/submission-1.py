class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        uniqueList = list(set(nums))
        return len(uniqueList) != len(nums)
        