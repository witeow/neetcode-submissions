class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        letter_count_dict = dict()

        for str_index in range(len(strs)):
            curr_str = strs[str_index]

            char_count = [0 for i in range(26)] # number of alphabets

            for letter in curr_str:
                char_count[ord(letter)-ord("a")] += 1
            
            char_count_hash = tuple(char_count)
            # print(char_count)
            # print(char_count_hash)

            if char_count_hash not in letter_count_dict:
                letter_count_dict[char_count_hash] = []
            letter_count_dict[char_count_hash].append(curr_str)

        # print(letter_count_dict.values())
        return list(letter_count_dict.values())
                
                
                
                
