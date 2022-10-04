class Solution:
    def fib(self, n: int) -> int:
        a, b = 1, 0
        if n <= 1:
           return n
            
        for i in range(2, n+1):
            a,b = a+b, a

        return a
