from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = [0,0]
        for x in range(len(nums)):
            partner = target - nums[x]
            for y in range(x+1,len(nums)):
                if partner == nums[y]:
                    indices = [nums[x],nums[y]]
                    print(indices)
                    return indices
        return -1

if __name__ == '__main__':
    s = Solution()
    s.twoSum([2,7,11,15],9)
