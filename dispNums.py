class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
    
        dictt = set()
        i = 1
        
        while i <= len(nums):
            dictt.add(i)
            i +=1

        for i in nums:
            dictt.discard(i)
            
        return dictt
        
