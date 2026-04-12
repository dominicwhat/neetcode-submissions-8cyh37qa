class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = Counter(nums)
        for freq in count.values():
            if freq != 1:
                return True
        return False
            
        