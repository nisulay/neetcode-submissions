class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for i in nums:
            required_j = target - i
            index_i = nums.index(i)
            
            #edge case of duplicate
            if required_j in nums[index_i + 1:]:
                index_j = nums.index(required_j, index_i + 1)
                return [index_i, index_j]

            if required_j in nums:
                index_j = nums.index(required_j)

                if index_j != index_i:
                    return [index_i, index_j]