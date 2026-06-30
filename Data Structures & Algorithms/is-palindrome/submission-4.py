class Solution:
    def isPalindrome(self, s: str) -> bool:
        left_ptr = 0
        right_ptr = len(s) - 1
        halfway = int(len(s)/2)

        while left_ptr < halfway and right_ptr>=halfway:
            if s[left_ptr].isalnum() == False:
                left_ptr += 1
                continue
            if s[right_ptr].isalnum() == False:
                right_ptr -= 1
                continue

            if s[left_ptr].lower() == s[right_ptr].lower():
                left_ptr += 1
                right_ptr -= 1
                continue
            else:
                return False
        return True