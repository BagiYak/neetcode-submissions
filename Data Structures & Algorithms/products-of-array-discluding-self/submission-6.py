class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        res = [1] * len(nums)
        pref = 1
        post = 1

        for i in range(len(nums)):
            res[i] = pref
            pref = pref * nums[i]

        for i in range(len(nums)-1, -1, -1):
            res[i] = res[i] * post
            post = post * nums[i]

        return res

# Time:  O(n)
# Space: O(1) auxiliary