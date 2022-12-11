class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        rSum = 0

        for i in nums:
            rSum += i
        
        lSum = 0

        for i in range(len(nums)):
            rSum -= nums[i]
            if lSum == rSum:
                return i
            lSum += nums[i]

        return -1
