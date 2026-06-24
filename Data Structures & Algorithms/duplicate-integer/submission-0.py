# https://neetcode.io/problems/duplicate-integer/history
# https://neetcode.io/problems/duplicate-integer/notes
## Solved in 10 min.

##First idea: Brute Force - check each num in the list using for loop twice:
# n = len(nums)
# for i in range(n):                # Outer loop goes from 0 to the end
#    for j in range(i + 1, n):     # Inner loop goes from next num to the end and checks nums
#        if nums[i] == nums[j]:
#            return True
# return False
# Understand that it's bad solution due to TimeComplexity `\(O(n^2)\)`

## Second idea: set() - TimeComplexity O(n) and MemoryComplexity O(n)

from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique = set()
        
        for num in nums:
            if num not in unique:
                unique.add(num)
            else:
                return True

        return False
