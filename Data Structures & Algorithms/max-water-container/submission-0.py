'''
algo 1: nested loop
O(n^2)

algo 2: inward pointers
O(n)
# init max_water
# init l, r
# while l < r
    # update max_water
    # move shorter height inward (this works because the shorter wall limits the max water, so if you move the taller wall in you can only get less water)
'''
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_water = 0
        l,r = 0,len(heights)-1
        while l < r:
            max_water = max(max_water, min(heights[l], heights[r]) * (r-l))
            if heights[l] < heights[r]: l += 1
            else: r -= 1
        return max_water
        