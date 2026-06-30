class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_set = {nums[0]:0}
        for num_index in range(1,len(nums)):
            subtracted = target-nums[num_index]
            print(subtracted)
            if (subtracted) in num_set:
                return [num_set.get(subtracted), num_index]
            num_set[nums[num_index]] = num_index