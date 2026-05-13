class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        #use set for large list
        new_set = set(nums)

        if len(new_set) == len(nums):
            return False
        else:
            return True

        # for i in range(len(nums)):

        #     x = nums[i]
        #     if nums.count(x) > 1:
        #         return True
            
        
        # return False
            
