class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []  # stores the rightmost value from each level
        q = collections.deque([root])  # start with the root node

        while q:
            rightSide = None  # reset the rightmost node for this level
            qLen = len(q)  # number of queue entries to process this round

            for i in range(qLen):
                node = q.popleft()  # remove and retrieve the front entry

                if node:  # skip None entries
                    rightSide = node  # overwrite with the latest real node
                    q.append(node.left)  # enqueue left before right
                    q.append(node.right)  # children wait for the next round

            if rightSide:  # this level contained at least one real node
                res.append(rightSide.val)  # save the last node's value

        return res