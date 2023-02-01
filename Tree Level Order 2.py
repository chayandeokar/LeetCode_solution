# 107. Binary Tree Level Order Traversal II

# https://leetcode.com/problems/binary-tree-level-order-traversal-ii/description/


class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        result , current = [], [root]
        while current:
            next_level, vals = [], []
            for node in current:
                vals.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            current = next_level
            result.append(vals)
        return result[::-1]
