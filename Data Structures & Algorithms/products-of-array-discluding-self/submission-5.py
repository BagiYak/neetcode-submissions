class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prodPref = 1
        prodPost = 1
        prefs = [0] * len(nums)
        posts = [0] * len(nums)
        res = [0] * len(nums)

        for i in range(len(nums)):
            prefs[i] = prodPref
            prodPref = prodPref * nums[i]

        for i in range(len(nums)-1, -1, -1):
            posts[i] = prodPost
            res[i] = prefs[i] * posts[i]
            prodPost = prodPost * nums[i]

        return res
            