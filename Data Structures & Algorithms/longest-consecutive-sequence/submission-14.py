class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums:
            return 0
        
        numsSet = set(nums)
        seq = 0
        for num in numsSet:
            if num - 1 not in numsSet:
                curSeq = 0
                curNum = num
                while curNum in numsSet:
                    curSeq += 1
                    curNum += 1
                if seq < curSeq:
                    seq = curSeq

        return seq