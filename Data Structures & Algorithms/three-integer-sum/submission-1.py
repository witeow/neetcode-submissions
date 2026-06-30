class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        sorted_nums = sorted(nums)

        ans = []

        for current_sum_index in range(len(sorted_nums)-2):

            # skip possible combinations for the same current_sum value
            if current_sum_index > 0 and sorted_nums[current_sum_index] == sorted_nums[current_sum_index-1]:
                continue
            else:
                # print(sorted_nums)
                smaller_pointer_index = current_sum_index + 1
                bigger_pointer_index =  len(nums)-1

                # as long as the index dont cross
                while smaller_pointer_index < bigger_pointer_index:
                    curr_sum = sorted_nums[current_sum_index] + sorted_nums[smaller_pointer_index] + sorted_nums[bigger_pointer_index]
                    increasing = 1
                    decreasing = 1
                    if curr_sum == 0:
                        ans.append([sorted_nums[current_sum_index], sorted_nums[smaller_pointer_index], sorted_nums[bigger_pointer_index]])
                        while sorted_nums[smaller_pointer_index] == sorted_nums[smaller_pointer_index+increasing] and (smaller_pointer_index+increasing)<bigger_pointer_index:
                            increasing +=1
                        while sorted_nums[bigger_pointer_index] == sorted_nums[bigger_pointer_index-decreasing] and (bigger_pointer_index-decreasing)>smaller_pointer_index:
                            decreasing +=1
                        smaller_pointer_index += increasing
                        bigger_pointer_index -= decreasing

                    # need bigger pointer to move left to decrease
                    elif curr_sum > 0:
                        while sorted_nums[bigger_pointer_index] == sorted_nums[bigger_pointer_index-decreasing] and (bigger_pointer_index-decreasing)>smaller_pointer_index:
                            decreasing +=1
                        bigger_pointer_index -= decreasing

                    # last case where sum < 0, hence need smaller pointer to move right to increase
                    else:
                        while sorted_nums[smaller_pointer_index] == sorted_nums[smaller_pointer_index+increasing] and (smaller_pointer_index+increasing)<bigger_pointer_index:
                            increasing +=1
                        smaller_pointer_index += increasing


        return ans
