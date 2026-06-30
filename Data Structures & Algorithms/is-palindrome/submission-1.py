class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(char for char in s if char.isalnum()).lower()
        halfway = int(len(s)/2)

        for i in range(halfway):
            if s[i] != s[len(s)-1-i]:
                return False
        return True