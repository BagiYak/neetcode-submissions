### Group Anagrams - medium ###
## Recommended solution from tip -> https://www.youtube.com/watch?v=vzdNOK2oB2E

# Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.
# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

# Example 1:
#   Input: strs = ["act","pots","tops","cat","stop","hat"]
#   Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]

# Example 2:
#   Input: strs = ["x"]
#   Output: [["x"]]

# Example 3:
#   Input: strs = [""]
#   Output: [[""]]

# Constraints:
#   1 <= strs.length <= 1000.
#   0 <= strs[i].length <= 100
#   strs[i] is made up of lowercase English letters.

# Topics:
#   Array, Hash table, String, Sorting

# Recommended Time & Space Complexity:
#   You should aim for a solution with O(m * n) time and O(m) space, where m is the number of strings and n is the length of the longest string.

## Hash Table - Recommended solution from tip:
#   Instead of sorting each string, we can represent every string by the frequency of its characters.
#   Since the problem uses lowercase English letters, a fixed-size array of length 26 can capture how many times each character appears.
#   Two strings are anagrams if and only if their frequency arrays are identical.
#   By using this frequency array (converted to a tuple so it can be a dictionary key), we can group all strings that share the same character counts.

# Algorithm:
#   Create a hash map where each key is a 26-length tuple representing character frequencies, 
#       and each value is a list of strings belonging to that anagram group.
#   For each string in the input:
#   Initialize a count array of size 26 with all zeros.
#   For each character c in the string, increment the count at the corresponding index.
#   Convert the count array to a tuple and use it as the key.
#   Append the string to the list associated with this key.
#   After processing all strings, return all the lists stored in the hash map.

### Time complexity: O(n⋅m)
### Space complexity: O(m)
### n - is the number of strings in the input list.
### m - is the maximum length of a string in the input list.

from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        res = defaultdict(list)

        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - ord("a")] += 1

            res[tuple(count)].append(s)

        return list(res.values())

