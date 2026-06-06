# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        in_id = {val:i for i, val in enumerate(inorder)}
        pre_id = 0

        def build(left, right):
            nonlocal pre_id

            if left > right:
                return None

            root_val = preorder[pre_id]
            pre_id += 1
            node = TreeNode(root_val)

            mid = in_id[root_val]

            node.left = build(left, mid - 1)
            node.right = build(mid + 1, right)

            return node

        return build(0, len(inorder) - 1)