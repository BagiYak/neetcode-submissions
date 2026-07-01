### Group Anagrams - medium ###
# https://neetcode.io/problems/anagram-groups/history?submissionIndex=0

## -> Solved in 1 hour and 10 min
# got tip - when used AI Claude looking for how to create in Python defaultdict(list) from collections import defaultdict
#   to be able to auto append without exception error -> I saw key = "".join(sorted(s))
#   it was after 1 hour trying to solve, so next 10 min I spent to write working code

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

### Idea-1: Brain storm ###
#
# create dict 'sMap' as 'key = str' -> 'value = list[str]': sMap = defaultdict(list) from collections import defaultdict
#
# loop a given array:
#   - create variable 'key' and join sorted string item: 'key = "".join(sorted(str))'
#       step by step 'key = "".join(sorted("tops"))' operations:
#           1) sorted("tops") - gives a letter list: ['o', 'p', 's', 't'] from string "tops"
#           2) "".join() - gives a string back from a letter list: "opst" (note: "" (empty string) means "no separator")
#           3) result key = "opst"
#               
#   - append to sMap 'key' as key and item as value: 'sMap[key].append(s)'
#
# return list of sMap values: 'list(sMap.values())'
#
### Time complexity: O(n⋅mlogm) - but recommended: O(m * n)
### Space complexity: O(n⋅m)    - but recommended: O(m)
### n - is the number of strings in the input list.
### m - is the maximum length of a string in the input list.

from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        sMap = defaultdict(list)

        for s in strs:
            key = "".join(sorted(s))
            sMap[key].append(s)

        return list(sMap.values())

