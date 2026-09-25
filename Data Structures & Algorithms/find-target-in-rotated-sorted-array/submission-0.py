'''
algo 1: 2 passes: binary search for rotation point, then binary search for target
1st pass:
    before: elem >= num[0]
    after: elem < num[0]
    return l
Then, determine if target is in left side or right side.
2nd pass:
    normal binary search
O(logn)

algo 2: binary search

'''
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def find_bounds():
            l,r = 0, len(nums)-1
            if nums[r] >= nums[0]: return l,r
            while r-l>1:
                mid = (r+l)//2
                if nums[mid] >= nums[0]: l = mid
                else: r = mid
            if nums[0] <= target <= nums[l]: return 0,l
            else: return r, len(nums)-1

        l,r = find_bounds()
        if nums[l] > target: return -1
        if nums[r] <= target:
            if nums[r] == target: return r
            else: return -1
        while r-l>1:
            mid = (r+l)//2
            if nums[mid] <= target: l = mid
            else: r=mid
        return l if nums[l]==target else -1
