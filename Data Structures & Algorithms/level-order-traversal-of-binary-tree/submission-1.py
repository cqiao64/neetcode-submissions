# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = [] # list to hold the levels what we are going to return

        q = collections.deque() # init quene to hold the nodes
        q.append(root) # add the root node to the quene

        while q: # while there's still nodes inside of the quene
            qLen = len(q) #how many nodes we need to iterate across
            level = [] # our collection of nodes at each level of the tree
            for i in range(len(q)): # iterating across each node in the bounds of total nodes
                node = q.popleft() # popping the first node in 
                if node:
                    level.append(node.val) # checks if node is non-null then appends it to this level's list
                    q.append(node.left) # adds the left child to the quene
                    q.append(node.right) # add the right child to the quene
            if level:
                res.append(level) # checks if there's any nodes at this level and if it does adds to the result before going back through the loop to process the child nodes in the previous step

        return res # return the list holding each level