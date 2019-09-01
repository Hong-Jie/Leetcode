#include <stdlib.h>
#include <stdio.h>


//Definition for singly-linked list.
typedef struct ListNode {
    int val;
    struct ListNode *next;
} tListNode;

struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) 
{
    tListNode* iterL1 = l1;
    tListNode* iterL2 = l2;
    tListNode* sum = malloc(sizeof(tListNode));
    tListNode* iterSum = sum;
    int carry = 0;

    tListNode* iterDummy = malloc(sizeof(tListNode));
    iterDummy->val = 0;
    iterDummy->next = NULL;
    
    while ((iterL1 != NULL) || (iterL2 != NULL))
    {
        if (iterL1 == NULL)
        {
            iterL1 = iterDummy;
        } 
        if (iterL2 == NULL)
        {
            iterL2 = iterDummy;
        }

        iterSum->val = (iterL1->val) + (iterL2->val) + carry;
        carry = (iterSum->val)/10; // The tens digit
        iterSum->val %= 10;  // The units digit
        
        iterL1 = iterL1->next;
        iterL2 = iterL2->next;
        if ((carry != 0) || (iterL1 != NULL) || (iterL2 != NULL))
        {
            iterSum->next = malloc(sizeof(tListNode));
            iterSum = iterSum->next;
        } 
    }

    if (carry != 0)
    {
        iterSum->val = carry;
    }
    iterSum->next = NULL;

    return sum;
}

int main()
{
    struct ListNode l15 = {.val=9,.next=NULL};
    struct ListNode l14 = {.val=4,.next=&l15};
    struct ListNode l13 = {.val=1,.next=&l14};
    struct ListNode l12 = {.val=3,.next=&l13};
    struct ListNode l11 = {.val=2,.next=&l12};
    struct ListNode* l1 = &l11;

    struct ListNode l24 = {.val=9,.next=NULL};
    struct ListNode l23 = {.val=3,.next=&l24};
    struct ListNode l22 = {.val=6,.next=&l23};
    struct ListNode l21 = {.val=9,.next=&l22};
    struct ListNode* l2 = &l21;

    tListNode* sum = addTwoNumbers(l1,l2);
    tListNode* iterSum = sum;

    printf("[%d]", iterSum->val);
    iterSum = iterSum->next;
    while (iterSum != NULL)
    {
        printf("->[%d]", iterSum->val);
        iterSum = iterSum->next;
    }
    printf("\n");

    return 0;
}
