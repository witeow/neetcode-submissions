class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        letter_count_dict = dict()

        for str_index in range(len(strs)):
            curr_str = sorted(strs[str_index]) # sorts the string alphabetically

            if curr_str == "":
                if "" not in letter_count_dict:
                    letter_count_dict[""] = []
                letter_count_dict[""].append("")
            
            else:
                # dictionary of letter as keys and number of occurence as values
                curr_dict = dict()
                
                for letter in curr_str:
                    curr_dict[letter] = curr_dict.get(letter, 0) + 1
                
                # if its a new length not in the letter_count_dict, we add the curr_dict to it
                # if len(curr_str) not in letter_count_dict:
                #     curr_dict["string"] = [curr_str]
                #     letter_count_dict[len(curr_str)] = [curr_dict]
                ## instead of using length of string to potentially reduce time complexity, we use the dictionary as a key
                ## this is possible as the alphabets are sorted, meaning the count of the letter will also be in order
                dict_to_str = ""
                for key, value in curr_dict.items():
                    dict_to_str += key + str(value)

                if dict_to_str not in letter_count_dict:
                    letter_count_dict[dict_to_str] = []
                # print(dict_to_str)
                # print(letter_count_dict)
                # print(letter_count_dict[dict_to_str])
                # print(type(letter_count_dict[dict_to_str]))
                letter_count_dict[dict_to_str].append(strs[str_index])

        ans = []
        # iterate through letter_count_dict
        for key, value in letter_count_dict.items(): 
            ans.append(value)

        return ans
                
                
                
                
