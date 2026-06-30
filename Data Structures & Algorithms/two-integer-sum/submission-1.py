### Two Sum ###

## Solved in 1 hour and 3 min.

# Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.
# You may assume that every input has exactly one pair of indices i and j that satisfy the condition.
# Return the answer with the smaller index first.

# Example 1:
#   Input: 
#   nums = [3,4,5,6], target = 7
#       Output: [0,1]
#           Explanation: nums[0] + nums[1] == 7, so we return [0, 1].

# Example 2:
#   Input: nums = [4,5,6], target = 10
#       Output: [0,2]

# Example 3:
#   Input: nums = [5,5], target = 10
#       Output: [0,1]

## Tech spec:
#   nums[i] + nums[j] == target
#   i != j

# Constraints:
#   2 <= nums.length <= 1000
#   -10,000,000 <= nums[i] <= 10,000,000
#   -10,000,000 <= target <= 10,000,000
#   Only one valid answer exists

### Idea-1: Broot force ###
# first loop and second inner loop
# check item with next one: nums[i] + nums[j] == target
# and if True return both indexes
# else return empty list
# bad solution due to time complexity O(n^2)


### Idea-2: Array Hash table (dict) ###
# One loop (index and num)
# save to dict, key is num and val is index: iMap[num] = index
# check target - num is present in dict: if True return indexes [iMap[target-num, 0], i] else return empty list []

class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:

        iMap = {}
        length = len(nums)

        if length < 2 or length >1000:
            return []

        for i, num in enumerate(nums):
            resultNum = target - num

            if resultNum in iMap:
                return [iMap[resultNum], i]

            iMap[num] = i

        return []






