### Top K Frequent Elements - medium ###
## Recommended solution from tip -> https://www.youtube.com/watch?v=YPTqKIgVk-k

# Given an integer array nums and an integer k, return the k most frequent elements within the array.
# The test cases are generated such that the answer is always unique.
# You may return the output in any order.

# Example 1:
#   Input: nums = [1,2,2,3,3,3], k = 2
#   Output: [2,3]

# Example 2:
#   Input: nums = [7,7], k = 1
#   Output: [7]

# Constraints:
#   1 <= nums.length <= 10^4.
#   -1000 <= nums[i] <= 1000
#   1 <= k <= number of distinct elements in nums.

# Recommended Time & Space Complexity
#   You should aim for a solution with O(n) time and O(n) space, where n is the size of the input array.

### 1 Idea ### -> spent 50 min. to see it's not accepted!
# 1 - if recommended time and space is O(n) - declare 'heap' and while looping push minus num to it 'heapq.heappush(heap, -num)'
# Then to get 'k' most frequent num within the input array:
# 2 - declare list 'result' []
# 3 - loop in range of len(heap)
# 4 - in a loop:
#   4.1 - if 'result' size == 'k' then return 'result'
#   4.2 - if '-heapq.heappop(heap)' is not in the list add it
# 5 - return list

### 2 - used Hint in AI ###
# Got hint while looking for 'collections.Counter' I've seen:
#   counts = collections.Counter([1, 2, 2, 3, 3, 3])
#   counts.most_common()        # [(3, 3), (2, 2), (1, 1)]  -- sorted by count, descending
#   counts.most_common(2)       # [(3, 3), (2, 2)]  -- top 2 most common
# so I used it because collections.Counter is already do what I was need to solve the problem

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        counts = collections.Counter(nums)

        result = []
        for item, freq in counts.most_common(k):    # unpack each tuple into item, freq
            result.append(item)

        return result
