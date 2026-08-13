class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        totalProduct = 1
        zeroCount = 0
        zeroIndex = -1

        for i, n in enumerate(nums):
            if n == 0:
                zeroCount += 1
                zeroIndex = i
                continue
            totalProduct *= n

        if zeroCount > 1:
            return [0] * len(nums)
            
        if zeroCount == 1:
            product = [0] * len(nums)
            product[zeroIndex] = totalProduct
            return product
            
        res = []
        for n in nums:
            res.append(int(totalProduct / n))
        
        return res