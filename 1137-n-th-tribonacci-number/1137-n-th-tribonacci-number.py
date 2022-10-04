class Solution:
    def tribonacci(self, n: int) -> int:
        a = precalculated = [0, 1, 1, 2, 4, 7, 13, 24, 44, 81, 149, 274, 504]
        lenA = len(a)
        if n < lenA:
           return a[n]                
        
        t0, t1, t2 = a[-3:]
        for i in range(lenA, n+1):
            t0, t1, t2 = t1, t2, t0+t1+t2
        return t2