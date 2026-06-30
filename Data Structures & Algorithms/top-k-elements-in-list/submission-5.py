class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq_arr = [[] for i in range(len(nums))]
        
        nums_count_map = {}

        for num in nums:
            nums_count_map[num] = nums_count_map.get(num, 0) + 1

        for number, count in nums_count_map.items():
            print(count)
            freq_arr[count-1].append(number)
            print(freq_arr)

        ans = []

        for i in range(len(freq_arr)-1, -1, -1):
            for num in freq_arr[i]:
                ans.append(num)
                if len(ans) == k:
                    return ans
        return ans