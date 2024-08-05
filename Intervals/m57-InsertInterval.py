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
    out=[]
    for i in range(len(intervals)):
        #Remember below flow
        if intervals[i][0] > interval[1]:
            out.append(interval)
            out.append(intervals[i:])
        elif(intervals[i][1] < interval[0]):
            out.append(intervals[i]) #Remember this and not inserting actual interval here
        else:
            interval=[min(interval[0], intervals[i][0]),
                      max(interval[1], intervals[i][1])]
    return out

print(insert([[1,3],[6,9]],[2,5]))