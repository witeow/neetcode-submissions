class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False

        letter_dict = dict()
        for letter in s:
            letter_dict[letter] = letter_dict.get(letter, 0) + 1

        for letter in t :
            if letter not in letter_dict:
                return False
            letter_dict[letter] -= 1
            if letter_dict[letter] == -1:
                return False
        return True 