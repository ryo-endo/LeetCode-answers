class Solution:
    def climbStairs(self, n: int) -> int:
        pp, p = 0, 1
        for _ in range(n):
            pp, p = p, (pp + p)
        return p
