#Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def bfs(self, subroot: TreeNode, side=1) -> list:
        queue = []
        array = []
        queue.append(subroot)
        
        while len(queue) != 0:
            node = queue.pop(0)
            if node == None:
                array.append("N")
                continue
            array.append(node.val)
            if side == 1:
                queue.append(node.left)
                queue.append(node.right)
            elif side == 2:
                queue.append(node.right)
                queue.append(node.left)
        
        return array
                
    
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        
        if root.left is None and root.right is None:
            return True
        
        if root.left and root.right:
            if root.left.val != root.right.val:
                return False            
            return self.bfs(root.left, 1) == self.bfs(root.right, 2)
        
        return False
