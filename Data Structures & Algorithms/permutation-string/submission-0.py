class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count = [0] * 26
        s1_count = [0] * 26
        if len(s1) > len(s2):
                return False

        for ch in s1:
            s1_count[ord(ch) - ord('a')] += 1
        for i in range(len(s1)):
            count[ord(s2[i]) - ord('a')] += 1

            if s1_count == count:
                return True
        left = 0
        for right in range(len(s1), len(s2)):
            count[ord(s2[right]) - ord('a')] += 1
            count[ord(s2[left]) - ord('a')] -= 1
            left += 1
            if s1_count == count:
                return True
        return False
            