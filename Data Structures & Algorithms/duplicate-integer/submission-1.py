class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        temp = set()
        for i in range(0, len(nums)):
            if nums[i] not in temp:
                temp.add(nums[i])
            else:
                return True

        return False 

        