class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        unique = list(set(ransomNote))
        for letter in unique:
            if letter not in magazine or ransomNote.count(letter) > magazine.count(letter):
                return False
        return True