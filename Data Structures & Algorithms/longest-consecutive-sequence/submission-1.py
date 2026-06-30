class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nums_set = set(nums)

        nums_map = {}
        max_arr = []
        max_length = 0
        for num in nums_set:

            if num-1 in nums_set:
                continue # we will iterate when it is not in set (which means the start of a sequence)
            else:
                curr_arr = []
                counter = 0
                while num+counter in nums_set:
                    curr_arr.append(num+counter)
                    counter += 1
                if counter > max_length:
                    max_arr = curr_arr
                    max_length = counter
        return max_length