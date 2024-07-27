"""
You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start
and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval
newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still
does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

Note that you don't need to modify intervals in-place. You can make a new array and return it.
"""

def insert(intervals, interval):
    i=0
    while i < len(intervals):
        if intervals[i][0] < interval[0]:
            i+=1
        else:
            if interval[0] < intervals[i-1][1]:
                start= intervals[i-1][0]
            else:
                start=interval[0]
            while interval[1] > intervals[i][1]:
                i+=1
            if interval[1] < intervals[i][0]:
                end = interval[1]
            else:
                end = intervals[i][1]
            break
    out=[]
    i=0
    while i < len(intervals):
        if intervals[i][0]<=start <=intervals[i][1]:
            intervalBegin=i
            while intervals[i][0]<=end<=intervals[i][1]:
                i+=1
            out.append([intervalBegin,i])
        out.append([intervals[i][0],intervals[i][1]])
        i+=1
    return out

print(insert([[1,3],[6,9]],[2,5]))