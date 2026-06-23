class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      for i in range(0, len(nums)):
        targetNum = target - nums[i]
        if targetNum in nums:
            for j in range(0, len(nums)):
                if i == j:
                    continue
                if nums[j] == targetNum:
                    return [i, j]   