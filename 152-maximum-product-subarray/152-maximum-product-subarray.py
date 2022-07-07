class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        #TCo(n)
        #SCo(1)
        ans=0
        currentProduct=1
        if len(nums)==1:
            return nums[0]
        for elem in nums:
            if (elem !=0):
                currentProduct=currentProduct*elem
                ans=max(currentProduct,ans)
            else:
                currentProduct=1
        currentProduct=1
        for i in range(len(nums)-1,-1,-1):
            if nums[i] !=0:
                currentProduct=currentProduct*nums[i]
                ans=max(currentProduct,ans)
            else:
                currentProduct=1
        return ans 