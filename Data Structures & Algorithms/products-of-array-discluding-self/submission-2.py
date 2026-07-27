# Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].

# Each product is guaranteed to fit in a 32-bit integer.
# Follow-up: Could you solve it in O(n) time without using the division operation?

# Example 1:
# Input: nums = [1,2,4,6]
# Output: [48,24,12,8]
#   -> output[0] = 2 * 4 * 6 = 48
#   -> output[1] = 1 * 4 * 6 = 24
# Example 2:
# Input: nums = [-1,0,1,2,3]
# Output: [0,-6,0,0,0]
#   -> output[0] = -6 * 0 * 0 * 0 = 0
#   -> output[1] = -1 * 1 * 2 * 3 = -6

# Constraints:
# 2 <= nums.length <= 1000
# -20 <= nums[i] <= 20

# Recommended Time & Space Complexity
# You should aim for a solution as good or better than O(n) time and O(n) space,
# where n is the size of the input array.

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        res = [1] * len(nums)

        # 1 loop
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix = prefix * nums[i]

        # 2 loop
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            # 'postfix' multiply to 'res[i]' - because in first loop we assigned it as prefix value
            res[i] = postfix * res[i]
            postfix = postfix * nums[i]

        return res

## 2 Solution (not using the division operation)
# Time and Space Complexity is O(N)

# YouTube tip -> https://www.youtube.com/watch?v=bNvIQI2wAjk