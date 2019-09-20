"""
Constraint:
1. non-empty
2. only 1, 0

Edge cases:

Save computing time:
1. Trailing left '0's
"""

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry=0
        sumBinary = ""
        
        if len(a) >= len(b):
            longer, shorter = a, b
        else:
            longer, shorter = b, a
            
        for rIdx in range(-1,-len(longer)-1,-1):
            intL = int(longer[rIdx])
            if rIdx >= -len(shorter):
                intS = int(shorter[rIdx])
                localSum = intL + intS + carry
            else:
                localSum = intL + carry
            carry = 0    
            if localSum > 1:
                carry = 1
                sumBinary = str(localSum-2) + sumBinary
            else:
                sumBinary = str(localSum) + sumBinary
        
        if carry == 1:
            sumBinary = '1' + sumBinary
            
        return sumBinary
