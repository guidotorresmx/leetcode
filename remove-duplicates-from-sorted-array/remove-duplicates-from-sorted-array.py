class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        head = 0
        prev_n = float('-inf')
        for i, n in enumerate(nums):
            if n != prev_n:
                prev_n = n
                nums[head] = n
                head += 1
        for i in range(head,len(nums)):        
            del nums[-1]
        return head +1 
        
        