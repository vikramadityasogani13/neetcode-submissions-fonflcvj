class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        character_s = {}
        character_t = {}

        for ch in s:
            character_s[ch] = character_s.get(ch,0) + 1
        for ch in t:
            character_t[ch] = character_t.get(ch,0) + 1
        return character_s == character_t