class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = 0
        j = len(nums) - 1
        while j >= i:
            middle = j - i // 2
            if nums[middle] == target:
                return middle
            elif nums[middle] > target:
                j = middle - 1
            else:
                i = middle + 1
        return -1 
