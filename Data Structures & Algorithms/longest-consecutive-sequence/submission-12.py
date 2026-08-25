class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if not nums:
            return 0

        s = set(nums)
        seqRes = 0
        for n in nums:
            if n-1 not in s:
                current = 1
                while n+1 in s:
                    current += 1
                    n += 1
                
                if seqRes < current:
                    seqRes = current

        return seqRes