class Solution:
    def romanToInt(self, s: str) -> int:
        symbols = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }

        sum = 0
        for i in range(0, len(s)):
            current = s[i]
            next = s[i+1:i+2]

            if next and symbols[current] < symbols[next]:
                sum -= symbols[current]
            else:
                sum += symbols[current]

        return sum
