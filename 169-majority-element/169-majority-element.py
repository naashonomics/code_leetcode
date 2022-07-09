class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Boyer-Moore Voting Algorithm
            count=0
            candidate=None
            for n in nums:
                if count == 0:
                    candidate=n
                count += (1 if n == candidate else -1 )
            return candidate
    
    def majorityElement_sort(self, nums: List[int]) -> int:
        #Time complexity : O(nlgn)
        #Space complexity : O(1)
        nums.sort()
        return nums[len(nums)//2]
    
    def majorityElement_hashmap(self, nums: List[int]) -> int:
        #Time complexity : O(n)
        #Space complexity : O(n)
        counts = collections.Counter(nums)
        return max(counts.keys(), key=counts.get)