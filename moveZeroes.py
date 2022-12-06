class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        x=0 #left pointer 
        y = 1 #right pointer

        while y < len(nums):
            #if left pointer points to non zero dont swap anything
            if nums[x] != 0:
                x+=1
            #if it does and our right pointer points to a non zero swap
            elif nums[y] != 0:
                nums[x] = nums[y]
                nums[y] = 0
                x+=1

            y+=1
            


