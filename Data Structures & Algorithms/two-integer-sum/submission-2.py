class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complement_map = {}
        for idx, num in enumerate(nums):
            if num in complement_map:
                return [complement_map[num], idx]
            else:
                complement_map[target - num] = idx
            