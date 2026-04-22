# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
r'''
       1
    /     \
   2       3
 /    \  /    \
4     5  6     7

inorder = [4,2,5,1,6,3,7]
preorder = [1,2,4,5,3,6,7]
return = [1,2,3,4,5,6,7]

'''
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        in_id, pre_id = 0, 0

        def dfs(limit):
            nonlocal in_id, pre_id
            if pre_id >= len(preorder):
                return None
            if inorder[in_id] == limit:
                in_id += 1
                return None

            root = TreeNode(preorder[pre_id])
            pre_id += 1
            root.left = dfs(root.val)
            root.right = dfs(limit)
            return root
        return dfs(float("inf"))

