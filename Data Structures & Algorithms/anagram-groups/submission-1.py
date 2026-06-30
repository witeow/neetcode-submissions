class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        letter_count_dict = dict()

        for str_index in range(len(strs)):
            curr_str = strs[str_index]
            if curr_str == "":
                letter_count_dict[0] = letter_count_dict.get(0, [{"string":[]}])
                letter_count_dict[0][0]["string"].append("")
            else:

                # dictionary of letter as keys and number of occurence as values
                curr_dict = dict()
                
                for letter in curr_str:
                    curr_dict[letter] = curr_dict.get(letter, 0) + 1
                
                # if its a new length not in the letter_count_dict, we add the curr_dict to it
                if len(curr_str) not in letter_count_dict:
                    curr_dict["string"] = [curr_str]
                    letter_count_dict[len(curr_str)] = [curr_dict]
                    
                else:
                    str_dict_list = letter_count_dict.get(len(curr_str))
                    appended = True

                    for string_dict in str_dict_list:
                        for letter, number in curr_dict.items():
                            print(f"Letter: {letter}")
                            print(f"Number: {number}")
                            if letter not in string_dict:
                                appended = False
                                break
                            if string_dict[letter] != curr_dict[letter]:
                                appended = False
                                break
                            appended = True

                        if appended == True:
                            print(string_dict["string"])
                            print(curr_str)
                            string_dict["string"].append(curr_str)
                            break
                    
                    if appended == False:
                        curr_dict["string"] = [curr_str]
                        str_dict_list.append(curr_dict)

        ans = []
        # iterate through letter_count_dict
        for key, value in letter_count_dict.items(): 
            for string_dict in value:
                ans.append(string_dict["string"])

        return ans
                
                
                
                
