class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums = sorted(nums)
        sum = 0
        toggler = True
        for i, n in enumerate(nums):
            if toggler:
                toggler = False
                sum += n
            else:
                toggler = True
                sum -=n
            
        return sum