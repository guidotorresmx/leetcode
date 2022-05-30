class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        tempString = ""
        maxLen = 0
        for char in s:
            if char in tempString:
                tempString = tempString[tempString.index(char)+1:]
            else:
                if len(tempString)+1 > maxLen:
                    maxLen = len(tempString)+1                                
            tempString+=char
        return maxLen