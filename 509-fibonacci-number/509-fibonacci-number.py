class Solution:
    def fib(self, n: int) -> int:
        a, b = 1, 0
        if n <= 1:
           return n
        if n<=5:            
            for i in range(2, n+1):
                a,b = a+b, a
            return a
        return pow(2 << n, n+1, (4 << 2 * n) - (2 << n)-1) % (2 << n)
