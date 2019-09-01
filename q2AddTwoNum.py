class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1:ListNode, l2:ListNode) -> ListNode:
        iterL1 = l1
        iterL2 = l2
        Sum = ListNode(0)
        iterSum = Sum 
        Dummy = ListNode(0)
        carry = 0

        while ((iterL1 is not Dummy) or (iterL2 is not Dummy)):
            iterSum.val = iterL1.val + iterL2.val + carry
            carry = (iterSum.val)//10 # The tens digit
            iterSum.val %= 10  # The units digit

            if iterL1.next is None:
                iterL1.next = Dummy
            if iterL2.next is None:
                iterL2.next = Dummy

            iterL1 = iterL1.next;
            iterL2 = iterL2.next;

            if ((carry != 0) or (iterL1 is not Dummy) or (iterL2 is not Dummy)):
                iterSum.next = ListNode(0)
                iterSum = iterSum.next

        if carry != 0:
            iterSum.val = carry
        
        iterSum = Sum
        while iterSum is not None:
            iterSum = iterSum.next
        
        return Sum

def assignListNodeNum(l:ListNode, ls:list):
    iterL = l
    for i, val in enumerate(ls):
        iterL.val = val
        if i < (len(ls)-1):
            iterL.next = ListNode(0)
        iterL = iterL.next

if __name__ == '__main__':
    s = Solution()
    List1 = [2,3,1,4,9]
    List2 = [9,6,3,9]
    l1 = ListNode(0)
    l2 = ListNode(0)
    
    assignListNodeNum(l1, List1)
    assignListNodeNum(l2, List2)

    s.addTwoNumbers(l1,l2)

