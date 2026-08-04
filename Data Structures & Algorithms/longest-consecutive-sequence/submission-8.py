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

        if not nums:
            return 0
        
        s = set(nums)
        resSeq = 1

        for n in s:

            if n - 1 not in s:
                newSeq = 1
                current = n

                while current + 1 in s:
                    current = current + 1
                    newSeq = newSeq + 1

                if resSeq < newSeq:
                    resSeq = newSeq
                
        return resSeq

# This is my second solution, got insight to use set()
# Asked the ChatGPT and he explaned we need to use 'while' inside 'for' loop
# to be able to count sequence for each n in nums
# Got the aim as good than O(n) time and O(n) space
# Spent about 50 min to understand that I need the tip from ChatGPT)