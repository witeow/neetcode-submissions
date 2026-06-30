class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        current= []

        for i in range(len(nums)-2):
            for j in range(i+1, len(nums)-1):
                for k in range(j+1, len(nums)):
                    if nums[i] + nums[j] + nums[k] != 0:
                        continue
                    else:
                        dup = False
                        for ans in current:
                            if set(ans) == set([nums[i], nums[j], nums[k]]):
                                dup = True
                                break
                        if dup == False:
                            current.append([nums[i], nums[j], nums[k]])

        return current
