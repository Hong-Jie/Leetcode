class Solution:
    def isParenthesis(self, c):
        return ((c=='(') or (c==')'))
    
    def isValid(self, s:str):
        count = 0
        
        for ch in s:
            if ch == '(':
                count += 1
            elif ch == ')':
                count -= 1
            if count < 0:
                return False
        return (count == 0)
        
    def removeInvalidParentheses(self, s: str) -> List[str]:
        
        if self.isValid(s):
            return [s]
        
        ans = []
        
        queue = []
        visited = set()
        reached = False
        
        queue.append(s)
        visited.add(s)
        while ( len(queue)>0 ):
            curStr = queue.pop(0)
            
            if self.isValid(curStr):
                ans.append(curStr)
                reached = True
            if reached: continue
            for i, ch in enumerate(curStr):
                if not self.isParenthesis(ch):
                    continue
                
                subStr = curStr[:i]+curStr[i+1:]
                if subStr not in visited:
                    queue.append(subStr)
                    visited.add(subStr)
                    
        return ans
