class Solution:
    def fib(self, n: int) -> int:
        a = [0, 1, 1, 2, 3, 5, 8, 13, 21]
        if n < len(a):
           return a[n]
    
        a = (1 + math.sqrt(5))/2
        b = (1 - math.sqrt(5))/2
        return int((a**n - b**n) / (a-b))