"""
algo 1: remove most overlapping interval until no overlaps remain
# map each interval to all overlapping intervals: O(n^2)
# while overlaps remain: O(n)
    # remove interval with most overlaps: O(n)
    # increment num_removed
# return num_removed
T: O(n^2)
S: O(n^2)

algo 2: sorting and greedily remove
# sort intervals by end
# prev_end = -inf
# removed = 0
# for interval in intervals
    # if next_int_start < prev_end
        # removed += 1
    # else, interval is kept, so update prev_end
[1,2],[1,4],[2,4]
1 2 3 4 5 6 7 8 9 10
 -
   ---
 -----
"""
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda t: t[1])
        prev_end = float('-inf')
        removed = 0
        for start, end in intervals:
            if start < prev_end: removed += 1
            else: prev_end = end
        return removed