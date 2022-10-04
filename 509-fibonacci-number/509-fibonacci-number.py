class Solution:
    def fib(self, n: int) -> int:
        a = [0, 1, 1, 2, 3, 5, 8, 13, 21]
        if n < len(a):
           return a[n]
    
    
        #from https://akuli.github.io/math-tutorial/fib.html
        return int((1.618033988749895**n - (-0.6180339887498949)**n)/2.23606797749979)