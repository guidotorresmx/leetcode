class Solution:        
    def longestPalindrome(self, s: str) -> str:
        def testPalindrome(i):
            iMaxLen1, iRes1 = testPalindromeOdd(i)
            iMaxLen2, iRes2 = testPalindromePair(i)
            if iMaxLen1 > iMaxLen2:
                return iMaxLen1, iRes1
            return iMaxLen2, iRes2
            
        def testPalindromeOdd(i):
            l, r = i, i            
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

        def testPalindromePair(i):
            l, r = i, i+1            
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
            iMaxLen, iRes = testPalindrome(i)
            if iMaxLen > maxLen:
                maxLen = iMaxLen
                res = iRes
        return res