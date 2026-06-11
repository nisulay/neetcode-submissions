class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        #save each to a set
        mainset = set()
        mainset.update(nums)

        seq_lenght = 0
    
        #increment through list
        for i in range(len(nums)):

            j = 0

            #check if there is a previous number and skip if so
            if nums[i] - 1 in mainset:
                continue

            #loop a counter 
            #if elemenet's next number is the set then valid
            #continue the next number and check again't set
            while (nums[i] + j in mainset):
                j +=1
                #keep track 
                seq_lenght = max(seq_lenght, j)

        return seq_lenght
        
        
        