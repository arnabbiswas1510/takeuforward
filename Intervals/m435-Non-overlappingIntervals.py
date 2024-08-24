""" Problem: Given an array of intervals where intervals[i] = [starti, endi], return the minimum number of
intervals you need to remove to make the rest of the intervals non-overlapping.

This is a Greedy algorithm - Apply the locally optimal solution at each step hoping that it results in the globally
optimal solution
1. sort by start time
2. if overlapping, greedily remove the interval with larger end time, i.e.,
pre_end_time = min(pre_end_time, curr_intervals_end_time);
otherwise, pre_end_time = curr_intervals_end_time
https://github.com/arnabbiswas1510/takeuforward/blob/3b59806edae4756d4c27018c5fa6c2657910ab84/images/Intervals/m435-Non-overlappingIntervals.png
"""

def eraseOverlapIntervals(intervals):
    intervals.sort(key=lambda x:x[0])
    prevEnd=intervals[0][1]
    remove=0
    for interval in intervals[1:]:
        if interval[0] < prevEnd:
            prevEnd=min(prevEnd,interval[1])
            remove+=1
        else:
            prevEnd=interval[1]
    return remove

print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]))