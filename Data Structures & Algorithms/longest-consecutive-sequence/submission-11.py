class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        s = set()
        for n in nums:
            s.add(n)

        a = [0] * len(s)
        print(f"a = {len(a)}")
        for n in s:
            seq = 1
            if n-1 in s:
                continue
            while n+1 in s:
                seq = seq + 1
                n = n + 1
            a[seq-1] = seq

        for i in range(len(a)-1, -1, -1):
            if a[i] > 0:
                return a[i]
        
        return 0