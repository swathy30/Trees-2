class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        self.target = targetSum
        self.result = []
        self.traversal(root,0,[])
        return self.result
    
    def traversal(self,root,currsum,path):
        if root == None:
            return
        
        path.append(root.val)
        currsum += root.val
        
        self.traversal(root.left,currsum,path)
        
        if root.left == None and root.right == None:
            if currsum == self.target:
                temp = path[:]
                self.result.append(temp)
                
        self.traversal(root.right,currsum,path)
        path.pop()