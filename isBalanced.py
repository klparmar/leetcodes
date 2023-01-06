# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        notEven = [0]

        def dfs(root) -> int:
            if not root:
                return 0
            left =dfs(root.left)
            right = dfs(root.right)

            if abs(left - right) > 1:
                notEven[0] = 1
            return 1+ max(left, right)

        if not root:
            return True
        
        result = abs(dfs(root .left) - dfs(root.right)) <= 1

        if notEven[0] == 1:
            return False

        return result
