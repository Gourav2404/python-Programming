class Solution:
    def checkTree(self, root: Optional[TreeNode]) -> bool:
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if root.val==root.left.val+root.right.val:
            return True
        return False