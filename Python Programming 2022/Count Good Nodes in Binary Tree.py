# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        queue = deque([(root, root.val)])
        count = 0
        
        while queue:
            node, max_val = queue.popleft()
            max_val = max(max_val, node.val)
            
            count += (node.val == max_val)
            
            if node.left: queue.append((node.left, max_val))
            if node.right: queue.append((node.right, max_val))
            
        return count