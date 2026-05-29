class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        temp = []
        for i in range(0, len(nums)):
            if nums[i] not in temp:
                temp.append(nums[i])
            else:
                return True

        return False 

        