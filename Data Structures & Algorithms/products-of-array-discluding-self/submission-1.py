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
        product = 1
        zeroIndex = -1
        zeroCount = 0
        for i, n in enumerate(nums):
            if n == 0:
                zeroCount += 1
                zeroIndex = i
            else:
                product *= n

        if zeroCount > 1:
            return [0] * len(nums)

        if zeroIndex > -1:
            output = [0] * len(nums)
            output[zeroIndex] = product
            return output

        output = [0] * len(nums)
        for i, n in enumerate(nums):
            output[i] = int(product / n)

        return output
## 1 Solution (using the division operation):
# - spent 12 min to read & understand question,
# - then paused time, but during the day thinked about it several times
# - sudenly before layed to sleep at night
# - solved in mind and then implemented here and got success)

# Time Complexity is O(N), where N is the length of the nums array.
# The code iterates through the array exactly once in the first loop and at most once in the second loop.
# Space Complexity is O(N), as a new output array of the same length as the original is created to store the result.
# The additional memory for variables (product, zeroCount, zeroIndex) is O(1).
