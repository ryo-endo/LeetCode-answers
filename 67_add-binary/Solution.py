class Solution:
    def addBinary(self, a: str, b: str) -> str:
        n = int(a, 2) + int(b, 2)
        # return f'{n:b}'
        return bin(n)[2:]