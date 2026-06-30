class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # cal prefix product
        prefix_prod = [1] # instantiate 1 as the left of the first element is nothing

        curr_prod = 1
        for num in nums[:-1]:
            curr_prod *= num
            prefix_prod.append(curr_prod)

        # to exclude self, we can use product of all num on the left of self x product of all num on right of self
        # print(prefix_prod)
        # to cal sufix product, we iterate from right to left
        curr_prod = 1
        for num_index in range(len(nums)-1, 0, -1):
            curr_prod *= nums[num_index]
            prefix_prod[num_index-1] *= curr_prod

        return prefix_prod