class Solution:
    def getNoOfSetBits(self, num:int)-> int:
        count=0
        for i in range(32):
            if ((num & (1 << i))>0):
                count+=1
        return count    
            
    def countBits(self, n: int) -> List[int]:
        #TC: O(n)
        #SC:O(1)
        res=[]
        for i in range(n+1):
            res.append(self.getNoOfSetBits(i))
        return res
        