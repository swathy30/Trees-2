class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        self.result = 0
        self.traversal(root,0)
        return self.result
    
    def traversal(self,root,currsum):
        
        if root == None:
            return
        
        self.traversal(root.left,currsum*10+root.val)
        
        self.traversal(root.right,currsum*10+root.val)
        
        if root.left == None and root.right == None:
            self.result += currsum *10 + root.val