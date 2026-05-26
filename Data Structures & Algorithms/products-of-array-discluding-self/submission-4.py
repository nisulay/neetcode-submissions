class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output_list = []

        for i in range(len(nums)):

            #create list exclusive of index
            pre = nums[:i]
            post = nums[i+1:]
            product_list = pre + post

            product = 1
            for j in range(len(product_list)):
                product = product * product_list[j]

            output_list.append(product)   


        return output_list