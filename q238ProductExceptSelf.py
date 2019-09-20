"""

input = [1, 2, 3, 4]
output = [24, 12, 8, 6]
           .   1  1  1
           2   .  2  2
           3   3  .  3
           4   4  4  .

"""

class Solution:
    def productExceptSelf(self, nums):
        if len(nums) == 1:
            return []

        left = []
        right = []
        tmp = 1
        for idx in range(len(nums)):
            left.append(tmp)
            tmp *= nums[idx]

        tmp = 1
        for rIdx in reversed(range(len(nums))):
            right.insert(0,tmp)
            tmp *= nums[rIdx]

        print(left)
        print(right)
        return [l*r for l, r in zip(left, right)]

if __name__ == "__main__":
    sol = Solution()
    number = [1,2,3,4]
    print(sol.productExceptSelf(number))
