class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dedup_set = set(nums)
        if len(dedup_set) < len(nums):
            return True
        return False