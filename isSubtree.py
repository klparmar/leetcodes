# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def isSubtree(root, subRoot):
            if not root and not subRoot:
                return True
            if root and subRoot and root.val == subRoot.val:
                return(isSubtree(root.left, subRoot.left) and isSubtree(root.right, subRoot.right))
            return False


        def dfs(root, subRoot):
            if not root:
                return False
            if not subRoot:
                return True
            elif root.val == subRoot.val:
                if isSubtree(root, subRoot):
                    return True
            return (dfs(root.left, subRoot) or dfs(root.right, subRoot))

        return dfs(root, subRoot)
            
