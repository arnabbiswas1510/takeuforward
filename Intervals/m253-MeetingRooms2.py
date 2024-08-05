import heapq
from typing import List

#Classic usage of Priority Queues or Heaps
#nlogn time and n space (assuming all meetings end up in the rooms array
def minMeetingRooms1(intervals: List[List[int]]) -> int:
    rooms=[]
    intervals.sort(key=lambda x:x[0])
    heapq.heappush(rooms, intervals[0][1]) #Uses minheap by default. How to use maxHeap?
    for interval in intervals[1:]:
        if interval[0] > rooms[0]:
            heapq.heappop(rooms)
        heapq.heappush(rooms, interval[1])
    return len(rooms)

#2 pointer approach, Same time (due to sorting) and space complexity as above
#This solution is agnostic to actual intervals, you just plot the start and end times in an array after sorting
def minMeetingRooms2(intervals: List[List[int]]) -> int:
    intervals.sort(key=lambda x:x[0])
    startTimes=[x[0] for x in intervals]
    intervals.sort(key=lambda x:x[1])
    endTimes=[x[1] for x in intervals]
    start,end,rooms=0,0,0
    while start < len(startTimes):
        if startTimes[start] < endTimes[end]:
            rooms+=1
        else:
            end+=1
        start+=1 #Had put this after line 25 instead and that changed the answer
    return rooms

print(minMeetingRooms2([[1,10],[2,7],[3,19],[8,12],[10,20],[11,30]]))