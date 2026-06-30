class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        products = 1
        zero_present = 0

        for num in nums:
            if num != 0:
                products *= num
            else:
                zero_present += 1

        print(f"Products: {products}")
        if zero_present > 1:
            return [0 for i in range(len(nums))]
        elif zero_present == 1:
            for num_index in range(len(nums)):
                if nums[num_index]==0:
                    nums[num_index] = products
                else:
                    nums[num_index] = 0
        else:
            for num_index in range(len(nums)):
                nums[num_index] = int(products / nums[num_index])
            

        return nums