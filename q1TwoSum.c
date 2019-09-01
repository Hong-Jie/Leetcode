#include <stdlib.h>
#include <stdio.h>

int* twoSum(int* nums, int numsSize, int target) {
    
    int partner;
    int *indices = malloc(2*sizeof(int));
    
    for (int idx=0; idx<numsSize; idx++)
    {
        partner = target - nums[idx];
        
        for (int idy=numsSize-1; idy>idx; idy--)
        {
            if (partner == nums[idy])
            {
                indices[0] = idx;
                indices[1] = idy;
                return indices;
            }
        }
    }
    return NULL;
}

int main()
{
    int arr[] = {2, 7, 11, 15};
    int arrSize = 4;
    int target = 9;

    int *indices = twoSum(arr, arrSize, target);
    if (indices != NULL)
    {
        printf("%d %d\n", indices[0], indices[1]);
        free(indices);
        return 0;
    }
    return -1;
}
