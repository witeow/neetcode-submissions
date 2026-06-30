class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        lowest_number = min(nums)
        highest_number = max(nums)

        count_arr = [0 for i in range(highest_number-lowest_number+1)]

        for num in nums:
            count_arr[num-lowest_number] += 1
            print(count_arr)

        highest_freq = max(count_arr)
        ans = []
        while len(ans) != k:
            ans.append(count_arr.index(max(count_arr))+lowest_number)
            count_arr[count_arr.index(max(count_arr))] = 0
            print(count_arr)
        return ans