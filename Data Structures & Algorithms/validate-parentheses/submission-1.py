class Solution:
    def isValid(self, s: str) -> bool:
        
        stored_char = []
        lookup = {
            ')': '(',
            '}': '{',
            ']': '[',
        }

        for char in s:
            print(char)
            if char == '(' or char == '{' or char == '[':
                stored_char.append(char)
            else:
                if len(stored_char) == 0:
                    return False
                elif lookup[char] != stored_char[-1]:
                    return False
                else:
                    stored_char.remove(lookup[char])

        if len(stored_char) != 0:
            return False
        return True 