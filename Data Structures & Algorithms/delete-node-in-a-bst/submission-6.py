# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root # we weren't able to find the key so we just return the root
        
        if key > root.val:
            root.right = self.deleteNode(root.right, key) # if the key is larger than we search everything to the right
        elif key < root.val:
            root.left = self.deleteNode(root.left, key) # if the key is smaller everything to the left
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            
            cur = root.right
            while cur.left:
                cur = cur.left
            
            root.val = cur.val

            root.right = self.deleteNode(root.right, root.val)

        return root