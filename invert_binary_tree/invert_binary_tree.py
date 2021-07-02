# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        def rec(node):
            temp = node.right
            node.right = node.left
            node.left = temp
            if node.left:
                rec(node.left)
            if node.right:
                rec(node.right)
        if root: rec(root)
        return root
