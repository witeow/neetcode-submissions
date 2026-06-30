class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(char for char in s if char.isalnum()).lower()
        print(s)
        halfway = int(len(s)/2)
        print(halfway)

        for i in range(halfway):
            print(s[i], s[len(s)-1-i])
            if s[i] != s[len(s)-1-i]:
                return False
        return True