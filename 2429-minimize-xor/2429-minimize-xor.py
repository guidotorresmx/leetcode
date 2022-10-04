class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        """
        :type num1: int   0b111_111 
        :type num2: int   0b101_010_101 xor 0b101_010_111 =  0b000_000_010
        :rtype: int
        """
        
        a = 0
        b = num2.bit_count()
        
        for i in range(32, -1, -1):
            if num1&(1<<i):
                b -= 1
                a ^= 1<<i
                if b == 0:
                    break
        #print(a, b)
        x = 0
        while b:
            while a&(1<<x):
                x += 1
            a ^= 1<<x
            b -= 1
        return a