class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        #create a helper frequency array
        arr = [0] * (len(nums) + 1)
        
        #loop thru input array, add 1 to frequency array when we get a umber
        for i in nums:
            arr[i] = 1
            
        #loop thru freq. array, any index w 0 means that number was not in og array so return that index
        for i in range(len(arr)):
            if arr[i] == 0:
                return i
