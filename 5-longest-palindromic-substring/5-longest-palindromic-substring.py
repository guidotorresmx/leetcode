class Solution:        
    def longestPalindrome(self, s: str) -> str:
        def testPalindromes(i):
            iMaxLen1, iRes1 = testPalindrome(i, i)
            iMaxLen2, iRes2 = testPalindrome(i, i+1)
            if iMaxLen1 > iMaxLen2:
                return iMaxLen1, iRes1
            return iMaxLen2, iRes2
            
        def testPalindrome(l, r):
            while r<len(s) and s[l]==s[r]  :
                l-=1
                r+=1
                if l<0 or r>=len(s):
                    break                    
            l+=1
            r-=1
                
            iRes = s[l:r+1]
            iMaxLen = len(iRes)
            return iMaxLen, iRes

        
        res = ""
        maxLen = -1
        for i, char in enumerate(s):
            iMaxLen, iRes = testPalindromes(i)
            if iMaxLen > maxLen:
                maxLen = iMaxLen
                res = iRes
        return res