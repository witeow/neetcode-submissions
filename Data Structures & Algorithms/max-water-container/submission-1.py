class Solution:
    def maxArea(self, heights: List[int]) -> int:

        left_pointer = 0
        right_pointer = len(heights)-1
        max_area = 0

        while left_pointer < right_pointer:
            
            if heights[left_pointer]<heights[right_pointer]:
                curr_area = (right_pointer - left_pointer) * heights[left_pointer]
                left_pointer += 1
            else:
                curr_area = (right_pointer - left_pointer) * heights[right_pointer]
                right_pointer -= 1
            if curr_area> max_area:
                max_area = curr_area
        
        return max_area

