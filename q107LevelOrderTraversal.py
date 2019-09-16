#Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if root == None:
            return []
        
        queue = []
        array = []
        
        queue.append((root,0))
        while len(queue) != 0:
            node, cost = queue.pop(0)
            if len(array)==cost:
                array.append([])
            array[cost].append(node.val)
            if node.left: 
                queue.append((node.left,cost+1))
            if node.right:
                queue.append((node.right,cost+1))
        
        array.reverse()
        return array
