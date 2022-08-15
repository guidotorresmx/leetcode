class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {']':'[',
                 '}':'{',
                 ')':'('
                 }
        openers = "[{("
        closers = "]})"
        stack = []
        try:
            for char in s:
                if char in openers:
                    stack.append(char)
                elif char in closers:
                    if pairs[char]==stack[-1]:
                        stack.pop()
                    else:
                        return False
            if stack:
                return False
            return True
        except:
            return False
            