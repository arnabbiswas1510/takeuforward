"""Optimal solution is to sort and check the end time of m(i) is < start time of m(i+1) """
from itertools import pairwise
from typing import List


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:

        intervals = sorted(intervals)

        for a, b in pairwise(intervals): #New Python method, returns first 2 items from list regardless of their
            # structure. Without pairwise it would have returned 0,30. Pairwise returns (0,30),(5,10)
            if a[1] > b[0]:
                return False
        return True

s=Solution()
print(s.canAttendMeetings([[0,30],[5,10],[15,20]]))