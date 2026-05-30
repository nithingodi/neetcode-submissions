class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        history_map ={}

        for index, num in enumerate(nums):
            rem= target- num

            if rem in history_map:
                return [history_map[rem], index]
            history_map[num] = index


