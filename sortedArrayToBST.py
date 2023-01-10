# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        def createTree(nums):
            if nums == []:
                return None
            
            left = 0
            right = len(nums) - 1
            mid = 0
            while left < right:
                left +=1
                right -=1
            
            mid = left
            left = 0
            right = len(nums) - 1
            treeNode = TreeNode()
            treeNode.val = nums[mid]

            treeNode.left = createTree(nums[left:mid])
            treeNode.right = createTree(nums[mid+1: right+1])
            return treeNode

        return createTree(nums)
