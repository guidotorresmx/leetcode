class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tempList = {}
        for i, num in enumerate(nums):
            if target - num in tempList:
                return [i, tempList[target-num]]
            tempList |= {num: i}
        else:
            return -1