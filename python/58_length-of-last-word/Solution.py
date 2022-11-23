class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()

        try:
            return len(s) - (s.rindex(' ') + 1)
        except ValueError:
            return len(s)
