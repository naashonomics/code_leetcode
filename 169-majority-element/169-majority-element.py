class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #Time complexity : O(nlgn)
        #Space complexity : O(1) or O(n)
        nums.sort()
        return nums[len(nums)//2]
    
    
    def majorityElement_hashmap(self, nums: List[int]) -> int:
        #Time complexity : O(n)
        #Space complexity : O(n)
        counts = collections.Counter(nums)
        return max(counts.keys(), key=counts.get)