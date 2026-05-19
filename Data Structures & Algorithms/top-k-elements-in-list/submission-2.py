class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = {}

        for num in nums:

             count[num] = count.get(num, 0) + 1 
              

        sorted_group = sorted(count, key = count.get,  reverse = True)


        print(sorted_group)

        return sorted_group[:k]