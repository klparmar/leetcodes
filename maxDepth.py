# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    depth = 1
    currMax = 0
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root:
            if self.depth >= self.currMax:
                self.currMax = self.depth
            self.depth +=1
            self.maxDepth(root.left)
            self.maxDepth(root.right)
            self.depth -=1
        return self.currMax
