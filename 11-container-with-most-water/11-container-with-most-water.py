class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxContainerL, maxContainerR = l,r = 0, len(height) -1
        maxCapacity = 0
        
        while l<r:
            capacity = (r-l)*min(height[l],height[r])
            if capacity > maxCapacity:
                maxCapacity = capacity
                maxContainerL, maxContainerR = l,r
            if height[l] > height[r]:
                r-=1
            else: 
                l+=1
        return maxCapacity