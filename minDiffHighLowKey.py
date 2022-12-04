class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        #sort as adjacent sorted numbers yield min num
        nums.sort()
        
        #create 2 pointers and best possible min value
        pt1 = 0
        pt2 = k - 1
        minn = float(inf)
        
        while pt2 < len(nums):
            minn = min(minn, nums[pt2] - nums[pt1]) #get the min off our current min and lowest and highest value in window
            #increment/slide the window
            pt1 +=1
            pt2 +=1
            
        return minn
