class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        myDict = {} # key is number and value is frequency of this number in nums array
        for i in range(len(nums)):
            num = nums[i]
            myDict[num] = myDict.get(num, 0) + 1 # counting frequency of number

        buckets = [[] for _ in range(len(nums) + 1)] # length should be same as nums
        for num, freq in myDict.items():
            buckets[freq].append(num)

        res = []
        for i in range(len(buckets) - 1, -1, -1):
            if not buckets[i]:
                continue

            for num in buckets[i]:
                res.append(num)

            if len(res) == k:
                return res