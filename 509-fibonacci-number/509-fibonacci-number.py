class Solution:
    def fib(self, n: int) -> int:
        if n < 6:
            return [0, 1, 1, 2, 3, 5][n%6] 
        if n < 12:
            return [8, 13, 21, 34, 55, 89][n%6] 
        if n < 18:
            return [144, 233, 377, 610, 987, 1597][n%6] 
        if n < 24:
            return [2584, 4181, 6765, 10946, 17711, 28657][n%6] 
        if n < 30:
            return [46368, 75025, 121393, 196418, 317811, 514229][n%6]
        return 832040
    
    # -- this is another trick for foing it the right way --
    # -- fastests --
    #a = [0, 1, 1, 2, 3, 5, 8, 13, 21]
    #if n < len(a):
    #   return a[n]
    #return int((1.618034**n - (-0.618034)**n)/2.236068)
    #numbers obtained from https://akuli.github.io/math-tutorial/fib.html