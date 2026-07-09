class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        p1 = 0
        p2 = len(numbers) -1
        sum = numbers[p1] + numbers[p2]

        while (sum != target):
        
            sum = numbers[p1] + numbers[p2]

            if sum > target:
                p2 += -1 
            
            if sum < target:
                p1 += 1
        
        return [p1 + 1, p2 +1]