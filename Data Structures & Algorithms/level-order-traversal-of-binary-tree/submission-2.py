class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []  # stores one list of values per level

        q = collections.deque()  # queue of nodes waiting to be processed
        q.append(root)  # add the root as one queue entry

        while q:  # continue while queue entries remain
            qLen = len(q)  # save the number of entries for this level
            level = []  # stores the current level's node values

            for i in range(qLen):  # process only this level's entries
                node = q.popleft()  # remove and retrieve the front entry

                if node:  # skip None entries
                    level.append(node.val)  # record this node's value
                    q.append(node.left)  # queue the left child for the next level
                    q.append(node.right)  # queue the right child for the next level

            if level:  # avoid adding an empty level
                res.append(level)  # save this level before processing the next

        return res  # return all levels from top to bottom