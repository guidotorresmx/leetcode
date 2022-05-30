class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        tempString = ""
        maxLen = 0
        for char in s:
            if char in tempString:
                tempString = tempString[tempString.index(char)+1:]
            tempString+=char
            if len(tempString) > maxLen:
                maxLen = len(tempString)                
        return maxLen