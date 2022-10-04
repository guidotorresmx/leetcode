class Solution:
    def fib(self, n: int) -> int:

        return pow(2 << n, n+1, (4 << 2 * n) - (2 << n)-1) % (2 << n)
