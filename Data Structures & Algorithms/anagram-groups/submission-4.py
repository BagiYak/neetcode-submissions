# Verdict:
# Use Algorithm 2 — same big-O complexity, but significantly better constant factors and cleaner code.
# This is the standard LeetCode approach for anagram grouping.

# The Key Difference:
# Algorithm 1 builds a dictionary then converts it to frozenset — extra overhead.
# Algorithm 2 uses a pre-allocated 26-element array — direct, no intermediate structures.
# python# Algorithm 1: Dictionary overhead
# cMap = {}  # Allocate dict
# for c in s:  # Build it
#     cMap[c] = ...
# frozenset(cMap.items())  # Convert to frozenset (hash all items)

# Time & Space Complexity
#                     Time              Space
# Algorithm 1:        O(N)             O(1) extra
# Algorithm 2:        O(N)             O(1) extra
# Where N = total characters across all strings

# Detailed Breakdown:
# Algorithm 1 (frozenset approach):
# pythonfor s in strs:
#     cMap = {}                          # O(1)
#     for c in s:                        # O(len(s))
#         cMap[c] = cMap.get(c, 0) + 1   
#     k = frozenset(cMap.items())        # O(k) where k ≤ 26
#     gAnagrams.setdefault(k, []).append(s)

# Per string: O(len(s)) + O(26) = O(len(s))
# Total: O(N) time, O(1) extra space per string

# Algorithm 2 (tuple approach):
# pythonfor s in strs:
#     count = [0] * 26                   # O(26) = O(1)
#     for c in s:                        # O(len(s))
#         count[ord(c) - ord("a")] += 1
#     res[tuple(count)].append(s)        # O(26) = O(1)

# Per string: O(26) + O(len(s)) = O(len(s))
# Total: O(N) time, O(1) extra space per string

# Algorithm 2 is BETTER 🏆
# # Algorithm 2: Direct computation
# count = [0] * 26  # Allocate once
# for c in s:  # Direct array access
#     count[ord(c) - ord("a")] += 1
# tuple(count)  # Convert to tuple (simpler)

# Why?
# ╔════════════════════════════╦═════════════════════════════════════╦═══════════════════════════════╗
# ║ Factor                     ║ Algorithm 1                         ║ Algorithm 2                   ║
# ╠════════════════════════════╬═════════════════════════════════════╬═══════════════════════════════╣
# ║ Time Constants             ║ Dict creation + frozenset hashing   ║ Simple array + tuple          ║
# ╠════════════════════════════╬═════════════════════════════════════╬═══════════════════════════════╣
# ║ Space per string           ║ O(26) dict + O(26) frozenset        ║ O(26) array                   ║
# ╠════════════════════════════╬═════════════════════════════════════╬═══════════════════════════════╣
# ║ Hashing Overhead           ║ frozenset hashing (more complex)    ║ tuple hashing (faster) ⭐     ║
# ╠════════════════════════════╬═════════════════════════════════════╬═══════════════════════════════╣
# ║ Readability                ║ Moderate                            ║ Clearer ⭐                     ║
# ╠════════════════════════════╬═════════════════════════════════════╬═══════════════════════════════╣
# ║ Practical Performance      ║ ~1.2x slower                        ║ Baseline ⭐                    ║
# ╚════════════════════════════╩═════════════════════════════════════╩═══════════════════════════════╝

# Algorithm-2 (with 26 array + tuple):
# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

#         res = defaultdict(list)

#         for s in strs:
#             count = [0] * 26

#             for c in s:
#                 count[ord(c) - ord("a")] += 1

#             res[tuple(count)].append(s)

#         return list(res.values())

# Algorithm-1 (with dict & frozenset hashing):
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        gAnagrams = {}

        for i, s in enumerate(strs):

            cMap = {}
            for c in s:
                cMap[c] = cMap.get(c, 0) + 1
            
            k = frozenset(cMap.items())
            gAnagrams.setdefault(k, []).append(s)

        return list(gAnagrams.values())
        