class Solution:
    def maxCrossArray(self, nums, mid):
        maxSum = float("-inf")
        tempSum = 0
        
        for leftIdx in reversed(range(mid+1)): # Count left: mid, mid-1, mid-2, ...
            tempSum += nums[leftIdx]
            maxSum = max(maxSum, tempSum)
            
        tempSum = maxSum
        for rightIdx in range(mid+1, len(nums)): # Count right: mid+1, mid+2, ...
            tempSum += nums[rightIdx]
            maxSum = max(maxSum, tempSum)
            
        return maxSum
    
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        
        middle = len(nums)//2
        
        maxLeftSub = self.maxSubArray(nums[:middle])
        maxRightSub = self.maxSubArray(nums[middle:])
        maxCrossSub = self.maxCrossArray(nums, middle)
        
        return max(maxLeftSub, maxRightSub, maxCrossSub)
