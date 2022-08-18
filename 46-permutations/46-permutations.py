class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        

        permutations = []
        

        def permutate(depth = 0, nums = [], current = []):
            if len(nums) == 0:
                permutations.append(current)
            for i, num in enumerate(nums):
                permutate(depth+1, nums[:i]+nums[i+1:], current+[num])

        permutate(0, nums, [])

        return permutations
