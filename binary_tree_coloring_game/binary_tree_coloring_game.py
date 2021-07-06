# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def btreeGameWinningMove(self, root: TreeNode, n: int, x: int) -> bool:
        def search(node, val):
            if not node: return None
            if node.val == val:
                return node
            else:
                return search(node.left, val) or search(node.right, val)
        
        def size_tree(node):
            if not node:
                return 0
            else:
                return 1 + size_tree(node.left) + size_tree(node.right)
        
        p1_node = search(root, x)
        
        if size_tree(p1_node) <= n // 2:
            # Win possible through parent
            return True
        else:
            left_size = size_tree(p1_node.left)
            right_size = size_tree(p1_node.right)
            if left_size > n - left_size or right_size > n - right_size:
				# Win possible through left or right child
                return True
            else:
                return False
