"""
The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value,
and the median is the mean of the two middle values.

For example, for arr = [2,3,4], the median is 3.
For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.

Hint:
The invariant of the algorithm is two heaps, small and large, each represent half of the current list. The length of
smaller half is kept to be n / 2 at all time and the length of the larger half is either n / 2 or n / 2 + 1 depend on
n's parity.

This way we only need to peek the two heaps' top number to calculate median.

Any time before we add a new number, there are two scenarios, (total n numbers, k = n / 2):

(1) length of (small, large) == (k, k)
(2) length of (small, large) == (k, k + 1)
After adding the number, total (n + 1) numbers, they will become:

(1) length of (small, large) == (k, k + 1)
(2) length of (small, large) == (k + 1, k + 1)
"""
import heapq
from heapq import heappushpop

class MeanFinder:
    def __init__(self):
        self.small = []  # the smaller half of the list, max heap (invert min-heap)
        self.large = []  # the larger half of the list, min heap

    def addNum(self, num): #Only remember this function, pay attn to how push and pop for max heap (use -ve) both times
        # I got this right the first time, yay!!
        if len(self.small) == len(self.large):
            heapq.heappush(self.large, -heappushpop(self.small, -num))
        else:
            heapq.heappush(self.small, -heappushpop(self.large, num))

    def findMedian(self):
        if len(self.small) == len(self.large):
            return float(self.large[0] - self.small[0]) /2.0 #- because small is Max Heap
        else:
            return float(self.large[0])

m=MeanFinder()
m.addNum(1)
m.addNum(2)
print(m.findMedian())
m.addNum(3)
print(m.findMedian())