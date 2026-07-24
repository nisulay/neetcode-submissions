class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        L = 0
        R = len(heights) -1
        best_area = 0
        search = True

        while search:

            width =  R - L
            length = min(heights[L], heights[R])
            area = width * length
            best_area = max(area, best_area)

            if heights[L] < heights[R]:
                L += 1
            else:
                R -= 1
            
            if L == R:
                search = False

            
        
        return best_area
        

