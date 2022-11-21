class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        dictt = {}
        diff = 0
        
        for i,x in enumerate(nums):
            diff = target - x
            
            if diff in dictt:
                return [i, dictt[diff]]
            
            if x not in dictt:
                dictt[x] = i