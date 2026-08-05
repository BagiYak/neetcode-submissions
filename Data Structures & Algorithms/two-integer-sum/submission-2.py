class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            key = target - nums[i]
            if key in d:
                return [d[key], i]
            else:
                d[nums[i]] = i
            