### Top K Frequent Elements - medium ###
## Recommended solution -> https://www.youtube.com/watch?v=YPTqKIgVk-k

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
# Time O(n + m log k), worst-case O(n log k)
# Space O(m), worst-case O(n)
## n = total number of elements
## m = number of unique elements (m ≤ n)

# Got hint while looking for 'collections.Counter' I've seen:
#   counts = collections.Counter([1, 2, 2, 3, 3, 3])
#   counts.most_common()        # [(3, 3), (2, 2), (1, 1)]  -- sorted by count, descending
#   counts.most_common(2)       # [(3, 3), (2, 2)]  -- top 2 most common
# so I used it because collections.Counter is already do what I was need to solve the problem

### 3 - Bucket Sort from neetcode video ###
## https://www.youtube.com/watch?v=YPTqKIgVk-k
# Time: O(n) - time complexity corresponds to the recommendation
# Space: O(n) - space complexity corresponds to the recommendation

# Step 1: Count frequencies
# Step 2: Create list of buckets
# Step 3: Place numbers into buckets
# Step 4: Collect 'k' most frequent elements

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # Step 1: Count frequencies
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        ## nums[4, 1, 1, 2, 2, 2, 3] -> count(1:2, 2:3, 3:1, 4:1)
        
        # Step 2: Create list of buckets
        # size = len(nums) + 1, because each num can be unique in the input array
        freq = [[] for _ in range(len(nums) + 1)]
        ## freq[ [], [], [], [], [], [], [] ]

        # Step 3: Place numbers into buckets
        # 'index' is a 'frequency' of each 'num' in the input array
        # 'key' is 'num' in the input array
        for num, c in count.items():
            freq[c].append(num)
        # nums [4, 1, 1, 2, 2, 2, 3] -> count {4:1, 1:2, 2:3, 3:1}
        #                                 │
        #                                 ▼
        # freq
        # index:    0    1       2      3     4   5   6   7
        #        [ [],  [4,3],  [1],   [2],   [], [], [], [] ]

        # Step 4: Collect k most frequent elements
        result = []
        for c in range(len(freq) - 1, 0, -1):
            for num in freq[c]:
                result.append(num)
                if len(result) == k:
                    return result
                    
        # nums [4, 1, 1, 2, 2, 2, 3] -> result [2, 1]

