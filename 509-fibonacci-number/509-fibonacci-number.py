class Solution:
    def fib(self, n: int) -> int:
        a = [0, 1, 1, 2, 3, 5, 8, 13, 21]
        if n < len(a):
           return a[n]
        return int((1.618034**n - (-0.618034)**n)/2.236068)