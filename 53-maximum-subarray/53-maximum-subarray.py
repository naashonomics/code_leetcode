class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsofar=nums[0]
        cursum=nums[0]
        for i in range(1,len(nums)):
            if (cursum <0):
                cursum=0
            cursum +=nums[i]
            if (cursum > maxsofar):
                maxsofar=cursum
        return  maxsofar