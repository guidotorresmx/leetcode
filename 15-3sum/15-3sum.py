class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        N, ans = len(nums), []

        def nextIndex(index, lastIndex):
            while index < lastIndex:
                index += 1
                if index == 0:
                    break
                if nums[index] == nums[index-1] :
                    continue
                else:
                    break
            return index

        i=-1
        while i < (N-2):

            i = nextIndex(i,N-2)
            j = i+1
            k = N-1

            while j<k:
                #print(f"indexes are {i} {j} {k} - values are {nums[i]} {nums[j]} {nums[k]}")
                sum = nums[i] + nums[j] + nums[k]
                if  sum == 0:
                    ans.append([nums[i], nums[j], nums[k]])
                    j = nextIndex(j,k)
                elif sum < 0:
                    j += 1
                else:
                    k -= 1
        return ans
