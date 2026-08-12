class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # result = []
        # for num, count in Counter(nums).most_common(k):
        #     result.append(num)
        # return result
        # or simple one line code:

        return [num for num, count in Counter(nums).most_common(k)]