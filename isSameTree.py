# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        listt = [[], []]
        def dfs(root ,index):
            if root:
                listt[index].append(root.val)
                dfs(root.left, index)
                dfs(root.right, index)
            else:
                listt[index].append(0)
                return
        dfs(p, 0)
        dfs(q, 1)

        return listt[0] == listt[1]
        
        
