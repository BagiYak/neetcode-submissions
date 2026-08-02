# Longest Consecutive Sequence

# Given an array of integers nums, return the length of the longest consecutive sequence of elements that can be formed.

# A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element. The elements do not have to be consecutive in the original array.

# You must write an algorithm that runs in O(n) time.

# Example 1:

# Input: nums = [2,20,4,10,3,4,5]

# Output: 4
# Explanation: The longest consecutive sequence is [2, 3, 4, 5].

# Example 2:

# Input: nums = [0,3,2,5,4,6,1,1]

# Output: 7
# Constraints:

# 0 <= nums.length <= 100,000
# -10^9 <= nums[i] <= 10^9

# Recommended Time & Space Complexity
# You should aim for a solution as good or better than
# O(n) time and O(n) space, where n is the size of the input array.

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if len(nums) == 0:
            return 0

        resCount = 0
        count = 0
        prevCount = 0
        lastPopped = -10**9
        heapq.heapify(nums)

        while nums:

            popped = heapq.heappop(nums)
            if popped == lastPopped:
                continue

            if popped == 1 + lastPopped:
                count = count + 1
            else:
                if count > prevCount:
                    prevCount = count
                count = 0

            lastPopped = popped

        if count > prevCount:
            resCount = count
        else:
            resCount = prevCount

        return resCount + 1

# spent 45 min to write code, but both cases had error
# I was sure that my idea in code should solve the problem
# so I asked ChatGPT to show only errors in my code
# then used his list of errors I refactored my code
# and then got Run success
# Time complexity: O(n)+O(nlogn) = O(nlogn)​
# - Runs n times
# - Each heappop() is O(log n)
# Space complexity: O(1)
# - heapq.heapify(nums) works in-place
# - Only variables are used (count, prevCount, etc.)