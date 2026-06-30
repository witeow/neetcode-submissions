class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = ""
        for string in strs:
            curr_string_length = int(len(string))
            ans += str(curr_string_length) + "#" + string
        return ans
            
    def decode(self, s: str) -> List[str]:
        index = 0
        ans = []
        while index != len(s):

            str_length = ""
            # read string until char is #
            while s[index] != "#":
                str_length += s[index]
                index += 1

            index += 1 # skip the #
            string = ""
            str_length = int(str_length)
            while str_length != 0:
                string += s[index]
                index += 1
                str_length -= 1

            ans.append(string)
        return ans

            

